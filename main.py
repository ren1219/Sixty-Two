import os
from PIL import Image

def scan_folder_for_images(input_folder, output_folder):
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist. Please create it and add skins.")
        return

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        try:
            with Image.open(input_path) as img:
                if img.size == (64, 32):
                    print(f"Processing image: {filename}")
                    process_image(img, filename, output_folder)
        except Exception as e:
            print(f"Skipping file {filename}: {e}")
            continue

def process_image(img, filename, output_folder):
    new_img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    new_img.paste(img, (0, 0))

    '''
    ARMS
    '''

    shoulder = img.crop((44, 16, 48, 20))
    shoulder_ = shoulder.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(shoulder_, (36, 48))

    hand = img.crop((48, 16, 52, 50))
    hand_ = hand.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(hand_, (40, 48))

    arm1 = img.crop((40, 20, 44, 32))
    arm1_ = arm1.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(arm1_, (40, 52))
    
    arm2 = img.crop((44, 20, 48, 32))
    arm2_ = arm2.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(arm2_, (36, 52))

    arm3 = img.crop((52, 20, 56, 32))
    arm3_ = arm3.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(arm3_, (44, 52))

    arm4 = img.crop((48, 20, 52, 32))
    arm4_ = arm4.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(arm4_, (32, 52))

    '''
    LEGS
    '''

    knee = img.crop((4, 16, 8, 20))
    knee_ = knee.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(knee_, (20, 48))

    shoe = img.crop((8, 16, 12, 50))
    shoe_ = shoe.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(shoe_, (24, 48))

    leg1 = img.crop((0, 20, 4, 32))
    leg1_ = leg1.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(leg1_, (24, 52))
    
    leg2 = img.crop((8, 20, 12, 32))
    leg2_ = leg2.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(leg2_, (16, 52))

    leg3 = img.crop((4, 20, 8, 32))
    leg3_ = leg3.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(leg3_, (20, 52))

    leg4 = img.crop((12, 20, 16, 32))
    leg4_ = leg4.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.paste(leg4_, (28, 52))

    output_path = os.path.join(output_folder, filename)
    new_img.save(output_path, "PNG")
    print(f"Done, saved to {output_path}")

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    scan_folder_for_images(input_folder, output_folder)