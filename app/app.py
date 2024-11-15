import pyautogui
import time


def search_and_click(images, confidence=0.7, offset_x=0, offset_y=0):
    for img in images:
        pos = pyautogui.locateOnScreen(img, confidence=confidence)
        if pos:
            pyautogui.click(pos.left + pos.width // 2 + offset_x, pos.top + pos.height // 2 + offset_y)
            return True
    return False


def att_shop():
    while True:
        found_shop = search_and_click(['CovenantbM.png', 'MysticBM.png', 'FriendshipBM.png'])
        
        if found_shop:
            time.sleep(0.5)  
            found_buy = search_and_click(['184gold.png', '18gold.png', '280value.png'], offset_y=50)
            
            if found_buy:
                time.sleep(0.5) 
                
                search_and_click(['Confirm.png'], confidence=0.8)
                time.sleep(1)
                continue
        else:
            pyautogui.scroll(-500)
            time.sleep(1)  

        found_buy = search_and_click(['184gold.png', '18gold.png', '280value.png'], offset_y=50)
        
        if not found_buy:
            refresh_clicked = search_and_click(['Refresh.png'])
            if refresh_clicked:
                time.sleep(0.5)
                search_and_click(['Confirm.png'], confidence=0.8)
        time.sleep(1)  


att_shop()
