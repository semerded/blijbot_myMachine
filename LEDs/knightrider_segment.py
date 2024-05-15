def main():
    from LEDs._segment import _Segment
    from time import sleep
    import board

    ledCount: int = 9
    knightRider = _Segment(board.D21, ledCount, 0.4)

    _currentLED = 0
    _ascending = True


    while True:
        data = knightRider.loadData("knightrider")
        
        knightRider.pixels[_currentLED] = data["color"]
            
        if _ascending and _currentLED > 0:
            knightRider.pixels[_currentLED - 1] = (0, 0, 0)
        elif not _ascending and _currentLED < ledCount - 1:
            knightRider.pixels[_currentLED + 1] = (0, 0, 0)
        
        if _currentLED == 0 and not _ascending:
            _ascending = True
        elif _currentLED == ledCount - 1 and _ascending:
            _ascending = False 
            
        _currentLED += 1 if _ascending else - 1
        
        sleep(data["speed"])