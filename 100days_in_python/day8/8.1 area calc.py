import math
def area_calc(height,weidth,cover):
    num_of_can=math.ceil((height*weidth)/cover)

    print(f"tou'll need {num_of_can} can of paint.")

test_h=int(input("height of wall : "))
test_w=int(input("width of wall : "))
coverage=5
area_calc(height=test_h,weidth=test_w,cover=coverage)
