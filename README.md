# Discord-Account-Generator

Create Discord Accounts Semi-Automatically without captcha solving api key

IMPORTANT: Your chromedriver version should be the same version as your chrome browser version!

Get chromedriver from here: <https://chromedriver.chromium.org/downloads>

![image](https://user-images.githubusercontent.com/48888771/126191568-14c99176-59c4-46b5-9f2e-cd720f8ee573.png)

## Feautures

+ Automatically generate username
+ Automatically generate password
+ Automatically generate email
+ Randomly choose date
+ Automatically get 0Auth token

## Future Goals

+ Verify account with temporary mail

# How to run

1. Install all the required python modules:

```py
pip install -r requirements.txt
```

4. Add proxy information and edit config inside account_generator.py:

```py
##############
proxy = "PROXY"  # Remember to enter your proxy
speedMultiplier = 5 # Higher speed = more difficult captcha
##########
```

3. To run this program, you should execute this:

```
python3 account_generator.py
```

You have to fill in the captcha! The program is made to not do it for you.
###### For legal reasons, don't use this. This was only made for educational purposes and is intended to be used as a learning opportunity for others.

If you like my creation, please consider starring the repo (:

### If you are looking for a more advanced, captcha solving included software, check it out on [Sellix!](https://sellix.io/product/60f039387a771)

(Closed Source so that Discord won't patch it!)

For other account generators: [Website](http://pigservices.piggyawesome.com)

[secret](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
