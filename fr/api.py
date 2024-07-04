import cv2
import face_recognition
import json
import os
import time
import numpy as np
import socket
import asyncio
#闯关弟子注意，本api库有两个函数，一个是用来注册人脸的，一个是用来检测人脸的
#注册人脸的函数是register_face()
#检测人脸的函数是process_video()
#注册人脸的时候会要求输入人脸的姓名，如果已经存在则会提示文件已存在
#检测人脸的时候会在5秒内检测到人脸则返回人脸的名字，否则返回Timeout
#人脸的名字是根据注册人脸的时候输入的名字来的
#本api由eh制作，如有问题请联系eh
#邮箱：zsyeh7286@gmail.com



#用来拍照
def add_face():
    # 打开摄像头
    #cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture('udp://@:1234')

    # 捕获一帧图像
    ret, frame = cap.read()

    # 保存图像
    name = input('请输入人脸的姓名：')
    #判断是否已经存在
    if os.path.exists('known_faces/' + name + '.jpg'):
        print('人脸已存在！')
        return '文件已存在！'
    cv2.imwrite('known_faces/' + name + '.jpg', frame)

    # 关闭摄像头
    cap.release()
#用来刷新json列表
def known_refresh():
    # Get a list of all image files in the 'known_faces' directory
    image_files = [f for f in os.listdir('known_faces') if f.endswith('.jpg') or f.endswith('.png')]

    # Initialize an empty list for storing face objects
    known_faces = []

    # Load each image file and compute face encodings
    for image_file in image_files:
        image = face_recognition.load_image_file(os.path.join('known_faces', image_file))
        face_encoding = face_recognition.face_encodings(image)[0]
        face_name = os.path.splitext(image_file)[0]  # Get the name of the image file without the extension
        known_faces.append({"name": face_name, "encoding": face_encoding.tolist()})

    # Write face data to a JSON file
    with open('face_encodings.json', 'w') as json_file:
        json.dump(known_faces, json_file)


def register_face():
    add_face()
    known_refresh()
    return '注册结束'

def detect_face(frame, known_face_encodings, known_face_names):
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    # rgb_small_frame = small_frame[:, :, ::-1]
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    # 假设 `small_frame` 是你的原始图像
    gray_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    return face_names

def process_video():
    # Load face data from a JSON file
    with open('face_encodings.json', 'r') as json_file:
        known_faces = json.load(json_file)

    # Extract known face encodings and names from the loaded data
    known_face_encodings = [np.array(face['encoding']) for face in known_faces]
    known_face_names = [face['name'] for face in known_faces]

    #video_capture = cv2.VideoCapture(0)
    video_capture = cv2.VideoCapture('udp://@:1234')

    start_time = time.time()
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        face_names = detect_face(frame, known_face_encodings, known_face_names)

        if face_names:
            print('Face detected:', face_names)
            return face_names[0]
            break

        if time.time() - start_time > 5:
            print('Timeout')
            return 'Timeout'
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()



def create_tcp_connection(ip, port):
    # 创建一个socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到指定的IP地址和端口号
    s.connect((ip, port))

    return s

def send_tcp_message(s, message):
    # 发送数据
    s.sendall(message.encode('utf-8'))


#异步发送数据

# async def send_tcp_message(ip, port, message):
#     reader, writer = await asyncio.open_connection(ip, port)

#     print(f'Send: {message!r}')
#     writer.write(message.encode())

#     data = await reader.read(100)
#     print(f'Received: {data.decode()!r}')

#     print('Closing the connection')
#     writer.close()
#     await writer.wait_closed()


#不关闭连接
async def send_tcp_message(ip, port, message):
    reader, writer = await asyncio.open_connection(ip, port)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')
#使用实例
#asyncio.run(api.send_tcp_message('192.168.238.13', 11452, 'hello\n'))



#异步接收数据
# async def receive_tcp_message(ip, port):
#     reader, writer = await asyncio.open_connection(ip, port)

#     data = await reader.read(100)
#     print(f'Received: {data.decode()!r}')

#     print('Closing the connection')
#     writer.close()
#     await writer.wait_closed()

async def receive_tcp_message(ip, port):
    reader, writer = await asyncio.open_connection(ip, port)

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')
    return data.decode()

#使用实例
# asyncio.run(api.receive_tcp_message('192.168.238.13', 11452）)