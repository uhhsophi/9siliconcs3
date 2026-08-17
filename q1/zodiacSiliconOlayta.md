def get_chinese_zodiac():
    zodiac_animals = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"
    ]
    while True:
        try:
            birthyear = int(input("Enter your birth year: "))
            
            if birthyear < 1900:
                print("Invalid Year, it should not be earlier than 1900")
                continue
            
            index = (birthyear - 1900) % 12
            zodiac = zodiac_animals[index]
            
            print(f"Your Chinese Zodiac Sign is: {zodiac}")
            break
            
        except ValueError:
            print("Please enter a valid numeric year.")
            
get_chinese_zodiac()

https://drive.google.com/file/d/1_y7Huu5k9fqdocTJO6BFIkw6TQZ3I1kA/view?usp=classroom_web&authuser=0



