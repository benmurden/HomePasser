HomePasser
==========

StreetPass from your home with your 3DS and Mac OSX.

HomePasser will pull from an extended list of MAC addresses used by the online HomePass community, shuffle them all up, then set your Mac's AirPort so that your 3DS will grab StreetPass tags automatically. At 10 tags, the application will pause, allowing you to deal with the visitors you have. From there you can enter the number of additional tags you need, or just hit return for another 10 more.

At any time when HomePasser is paused and you've had enough StreetPassin', just type 'q' and hit return.

## Setup

HomePasser will require that you have configured your Mac with Internet Connection Sharing at least once with the following settings.

* Share to other users on AirPort
* Access point name (SSID) is "attwifi"
* No security

Once you have configured these settings, you can turn off Internet Connection Sharing and begin using HomePasser.

## Usage

Navigate to the HomePasser directory in a terminal window and run the following command.

```
sudo python homepasser.py
```

You'll be asked for your Mac password, because of the sudo command. HomePasser requires escelated privileges in order to turn sharing on and off and set MAC addresses.

The default AirPort interface used is en1, but if you need to change this, use the following command format.

```
sudo python homepasser.py -i <interface>
```

So if your AirPort is on en0, for example, you would invoke HomePasser with the command below.

```
sudo python homepasser.py -i en0
```

### Options

For a list of additional options, run homepasser with the '-h' argument.

```
python homepasser.py -h
```

