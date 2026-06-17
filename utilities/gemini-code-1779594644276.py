import time
import sys
from matrix_ticker import TickerEngine

# --- RGB MATRIX CONFIGURATION ---
# If you are using hzeller's rpi-rgb-led-matrix library, uncomment the block below:
#
# from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
# options = RGBMatrixOptions()
# options.rows = 32
# options.cols = 64
# options.chain_length = 1
# options.parallel = 1
# options.hardware_mapping = 'regular' # or adafruit-hat
# matrix = RGBMatrix(options = options)
# canvas = matrix.CreateFrameCanvas()
# font = graphics.Font()
# font.LoadFont("fonts/6x10.bdf") # Ensure you have a valid font path
# text_color = graphics.Color(255, 255, 255)
# ---------------------------------

def main():
    engine = TickerEngine()
    
    print("Starting Sports Ticker Engine...")
    
    last_api_update = 0
    update_interval = 30  # Fetch new data every 30 seconds
    display_text = "Loading sports data..."
    
    # Mock X position for scrolling animation tracking
    x_pos = 64 

    try:
        while True:
            current_time = time.time()
            
            # Fetch fresh API data without blocking your matrix animation loop
            if current_time - last_api_update > update_interval:
                print("Fetching real-time updates from ESPN...")
                display_text = engine.get_next_display_text()
                last_api_update = current_time
                print(f"Current Ticker Text: {display_text}")

            # --- HARDWARE SCROLL LOGIC ---
            # If using actual hardware, uncomment this block to handle the matrix scroll:
            #
            # canvas.Clear()
            # len_pixels = graphics.DrawText(canvas, font, x_pos, 20, text_color, display_text)
            # x_pos -= 1
            # if x_pos < -len_pixels:
            #     x_pos = canvas.width
            # canvas = matrix.SwapOnVSync(canvas)
            # time.sleep(0.03) # Adjusts scroll speed animation
            # ------------------------------

            # Local fallback console tracker so you can see it work without hardware attached
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting Ticker.")
        sys.exit(0)

if __name__ == "__main__":
    main()