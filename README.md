# offlow

##Inspiration

Coming from a developing country like India with just 18% Internet Penetration and 800m of non-smartphone users, the issue of increasing internet outreach is very important. We wanted to leverage the capabilities of existing systems of cellular networks to make this possible.

## Check it out!
[![alt tag](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/423/647/datas/gallery.jpg)](https://www.youtube.com/watch?v=FXNgxycVW3E)

##What it does

To solve this problem we have come up with a personal assistant which lets you do a lot of things like setting reminders, location-based suggestions, answers to your queries ranging from the solution of mathematical equations to the nearest fuel station, and the best part - All of this is offline! Also, on top of it, we are making cross-platform offline payments possible through ultrasonic waves.

This solution requires the most basic hardware in a device (only a speaker and microphone) and is feasible in situations where there is no internet connection. A best use case is making payments between a retailer and customer offline and doing communication during a natural disaster when there is no network.

##How we built it

There are two parts of our hack:

    1.An offline, SMS-based personal assistant
    2.Sharing data across all nearby devices via gestures and messaging app in stock android without using any extra hardware or cellular networks.

**The offline SMS-** based query search engine is similar to a virtual assistant which sends responses to the user using our search API backed by powerful platforms like Wolfram and Target. The app is made by extending the existing messenger of stock android. So, no need to install any separate app!

**Sharing data** is made possible by using **Audio waves, specifically - Ultrasonic waves**, which can carry data efficiently and are inaudible to human ears, the best use case is offline payments. These audio waves are processed and made suitable for transmission using Fourier transform algorithm in Java. The security of data is ensured by using TOTP (Time-based One time password) mechanism.

##Challenges we ran into

Utilising existing resources and the modulation and demodulation of audio waves efficiently was a big challenge for us, along with the security while transmitting the data. Since, we extended the stock android messaging app, diving into the code and modifying it was another blockhead.

##Accomplishments that we're proud of

We were successfully able to demonstrate the use case of offline payments in the application and made a virtual assistant that works completely offline. The two apps are combined via native android messaging app so use will not have to download any external application. Our payment solution works even when both the mobile devices are in Airplane Mode.

##What we learned

We learned the use of Fourier transforms in processing the Audio signals along with the use CRC algorithms which maintain the integrity of data being transmitted. We explored the APIs of Target and Wolfram to improve the quality of our personal assistant's responses. Most importantly, we learned how data can be transmitted without a network connection and external hardware, which can be helpful in providing internet access in developing and underdeveloped countries.

##What's next for Offlow

We are looking forward to extend the offline data transfer to images and videos as well using Audio or Wifi Signals without using a network connection. Larger payloads would need to be chunked across several error corrected packets, which requires client and server support for it. We can experiment to find the range of frequencies that can reliably be transmitted and recorded. A wider range means more chunk bits, which directly impacts throughput. We are also looking forward to make a automated voice based personal assistant (Off-siri) utilizing the toll free calling capabilities.
