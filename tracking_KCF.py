import cv2
import csv
import os
import keyboard
videoPath = "C:\\Users\\82104\\Desktop\\차도가 아닌곳\\"
actionlist = os.listdir(videoPath)
action = 0
play = True
while action < len(actionlist):
    v = actionlist[action].split(".")[-1]
    print(v)
    if v=='mp4':
        try:
            if play==True:
                flag = True
                cap = cv2.VideoCapture(videoPath + actionlist[action])
                success,frame = cap.read()
                label1_result = []
                total1 = []
                label2_result = []
                total2 = []
                f1 = open(videoPath+'label1.csv','a',newline='')
                f2 = open(videoPath+'label2.csv','a',newline='')
                wr1 = csv.writer(f1)
                wr2 = csv.writer(f2)
                isRecording = True
                cnt = 0
                tracker = cv2.TrackerKCF_create()
                tracker1 = cv2.TrackerKCF_create()
                while cap.isOpened():
                    cnt = cnt + 1
                    success, frame = cap.read()
                    success1, frame = cap.read()
                    frame = cv2.resize(frame, (640, 480))
                    if not success:
                        break
                    if success:
                        success, boxes = tracker.update(frame)
                        success1, boxes1 = tracker1.update(frame)
                        if isRecording:
                            x = boxes[0] + boxes[2] / 2
                            y = boxes[1] + boxes[3] / 2
                            if x!=0 and y!=0:
                                total1.append((((boxes[0] + boxes[2]) / 2), ((boxes[1] + boxes[3]) / 2)))
                                label1_result.append((cnt,(int(boxes[0] + boxes[2]) / 2), (int(boxes[1] + boxes[3]) / 2),
                                                    abs((total1[len(total1) - 1][0] - total1[len(total1) - 2][0])),
                                                    abs((total1[len(total1) - 1][1] - total1[len(total1) - 2][1])),0))
                            # 중앙점 x 좌표, 중앙점 y좌표,중앙점 x좌표 변화량,중앙점 y좌표 변화량,Label
                            #print(label1_result)
                        p1 = (int(boxes[0]), int(boxes[1]))
                        p2 = (int(boxes[0] + boxes[2]), int(boxes[1] + boxes[3]))
                        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
                    if success1:
                        if isRecording:
                            x = boxes1[0] + boxes1[2] / 2
                            y = boxes1[1] + boxes1[3] / 2
                            if x != 0 and y != 0:
                                total2.append((((boxes1[0] + boxes1[2]) / 2), ((boxes1[1] + boxes1[3]) / 2)))
                                label2_result.append((cnt,(int(boxes1[0] + boxes1[2]) / 2), (int(boxes1[1] + boxes1[3]) / 2),
                                                    abs((total2[len(total2) - 1][0] - total2[len(total2) - 2][0])),
                                                    abs((total2[len(total2) - 1][1] - total2[len(total2) - 2][1])),1))
                            # 중앙점 x 좌표, 중앙점 y좌표,중앙점 x좌표 변화량,중앙점 y좌표 변화량,Label
                            #print(boxes1)
                        p3 = (int(boxes1[0]), int(boxes1[1]))
                        p4 = (int(boxes1[0] + boxes1[2]), int(boxes1[1] + boxes1[3]))
                        cv2.rectangle(frame, p3, p4, (0, 0, 255), 2, 1)
                    cv2.imshow('frame',frame)
                    k = cv2.waitKey(60) & 0xFF
                    if k==27:
                        break
                    if k == ord('i'):
                        bbox = cv2.selectROI('Multitracker', frame)
                        result = tracker.init(frame, bbox)
                    if k==ord('u'):
                        bbox2 = cv2.selectROI('Multitracker', frame)
                        result = tracker1.init(frame, bbox2)
                    if k==ord('o'):
                        if isRecording==True:
                            isRecording = False
                        else:
                            isRecording = True
                play = False
                while True:
                    if keyboard.is_pressed('p'):
                        if flag==True:
                            print(label1_result)
                            for i in range(len(label1_result)):
                                wr1.writerow([actionlist[action],label1_result[i][0], label1_result[i][1], label1_result[i][2], label1_result[i][3],
                                              label1_result[i][4],label1_result[i][5]])
                            for j in range(len(label2_result)):
                                wr2.writerow([actionlist[action],label2_result[j][0], label2_result[j][1], label2_result[j][2], label2_result[j][3],
                                              label2_result[j][4],label2_result[j][5]])
                            print('finish')
                            f1.close()
                            f2.close()
                            flag = False
                            cap.release()
                            cv2.destroyAllWindows()
                    if keyboard.is_pressed('s'):
                        action = action + 1
                        play = True
                        f1.close()
                        f2.close()
                        cap.release()
                        cv2.destroyAllWindows()
                        break
                    if keyboard.is_pressed('a'):
                        play = True
                        f1.close()
                        f2.close()
                        cap.release()
                        cv2.destroyAllWindows()
                        break
        except Exception as e:
                print(str(e))
                while True:
                    if keyboard.is_pressed('p'):
                        if flag == True:
                            print(label1_result)
                            for i in range(len(label1_result)):
                                wr1.writerow([actionlist[action], label1_result[i][0], label1_result[i][1], label1_result[i][2],
                                              label1_result[i][3],
                                              label1_result[i][4], label1_result[i][5]])
                            for j in range(len(label2_result)):
                                wr2.writerow([actionlist[action], label2_result[j][0], label2_result[j][1], label2_result[j][2],
                                              label2_result[j][3],
                                              label2_result[j][4], label2_result[j][5]])
                            print('finish')
                            f1.close()
                            f2.close()
                            flag = False
                            cap.release()
                            cv2.destroyAllWindows()
                    if keyboard.is_pressed('s'):
                        action = action + 1
                        play = True
                        f1.close()
                        f2.close()
                        cap.release()
                        cv2.destroyAllWindows()
                        break
                    if keyboard.is_pressed('a'):
                        play = True
                        f1.close()
                        f2.close()
                        cap.release()
                        cv2.destroyAllWindows()
                        break
    else:
        action = action + 1