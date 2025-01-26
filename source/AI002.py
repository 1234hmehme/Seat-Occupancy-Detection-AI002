import cv2
import numpy as np

VIDEO_SOURCE = 'MINH7.mp4'  
DIFF_THRESHOLD = 4_700_000 


seats = [
    {
        "name": "Seat 1",
        "x": 100, "y": 300, "w": 170, "h": 160,
        "background": None,
        "map_x": 140,  "map_y": 275, "map_w": 50, "map_h": 50
    },
    {
        "name": "Seat 2",
        "x": 500, "y": 300, "w": 170, "h": 160,
        "background": None,
        "map_x": 310, "map_y": 275, "map_w": 50, "map_h": 50
    },
    {
        "name": "Seat 3",
        "x": 200, "y": 100, "w": 170, "h": 160,
        "background": None,
        "map_x": 140,  "map_y": 175, "map_w": 50, "map_h": 50
    }
]

def main():
    cap = cv2.VideoCapture(VIDEO_SOURCE)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video is ended")
            break
        map_width, map_height = 500, 500
        map_img = np.full((map_height, map_width, 3), 200, dtype=np.uint8)  


        top_left = (200,150)
        bottom_right = (300,350)


        cv2.rectangle(map_img, top_left, bottom_right, (100, 80, 50), -1)
                

        for seat in seats:
            x, y, w, h = seat["x"], seat["y"], seat["w"], seat["h"]
            seat_roi = frame[y : y + h, x : x + w]

  
            if seat["background"] is None:
                seat["background"] = seat_roi.copy()
                continue

            # Compare current seat ROI to background
            diff = cv2.absdiff(seat_roi, seat["background"])
            diff_b, diff_g, diff_r = cv2.split(diff)
            diff_sum = (cv2.sumElems(diff_b)[0] +
                        cv2.sumElems(diff_g)[0] +
                        cv2.sumElems(diff_r)[0])


            occupied = diff_sum > DIFF_THRESHOLD


            mx, my, mw, mh = seat["map_x"], seat["map_y"], seat["map_w"], seat["map_h"]
            map_color = (0, 0, 255) if occupied else (0, 255, 0)  
            cv2.rectangle(
                map_img,
                (mx, my),
                (mx + mw, my + mh),
                map_color,
                -1  
            )

            cv2.putText(map_img, seat["name"], (mx, my - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)


        cv2.imshow("Main Frame", frame)
 
        cv2.imshow("Seat Map", map_img)


        key = cv2.waitKey(16) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('b'):
            print("Recapturing backgrounds for all seats...")
            for seat in seats:
                x, y, w, h = seat["x"], seat["y"], seat["w"], seat["h"]
                seat["background"] = frame[y : y + h, x : x + w].copy()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
