import sys, getopt, time
from subprocess import call
from random import shuffle
from optparse import OptionParser

def main(argv):

        parser = OptionParser(usage='usage: homepasser.py -i <interface> [options]')
        parser.add_option('-i', '--interface', dest='interface', help='The AirPort interface name. Default: en1', default='en1')
        parser.add_option('-n', '--no-shuffle', action='store_false', dest='shuffle', help='Turn off MAC address list shuffling.', default=True)
        parser.add_option('-p', '--no-pause', action='store_false', dest='pause', help='Just blow through the whole list of MAC addresses.', default=True)
        (options, args) = parser.parse_args()

        addr = ['00:0D:67:15:2D:82',
        '00:0D:67:15:D7:21',
        '00:0D:67:15:D5:44',
        '00:0D:67:15:D2:59',
        '00:0D:67:15:D6:FD',
        '4E:53:50:4F:4F:40',
        '4E:53:50:4F:4F:41',
        '4E:53:50:4F:4F:42',
        '4E:53:50:4F:4F:43',
        '4E:53:50:4F:4F:44',
        '4E:53:50:4F:4F:45',
        '4E:53:50:4F:4F:46',
        '4E:53:50:4F:4F:47',
        '4E:53:50:4F:4F:48',
        '4E:53:50:4F:4F:49',
        '4E:53:50:4F:4F:4A',
        '4E:53:50:4F:4F:4B',
        '4E:53:50:4F:4F:4C',
        '4E:53:50:4F:4F:4D',
        '4E:53:50:4F:4F:4E',
        '4E:53:50:4F:4F:4F',
        '00:25:9C:52:1C:6A',
        '00:0F:F7:00:2D:82',
        '50:3D:E5:75:50:62',
        '00:1A:A2:A2:17:23',
        '00:1F:CA:60:42:80',
        '00:22:55:C4:CC:10',
        '00:0F:8F:71:2E:A2',
        '4E:53:50:4F:4F:00',
        '4E:53:50:4F:4F:01',
        '4E:53:50:4F:4F:02',
        '4E:53:50:4F:4F:03',
        '4E:53:50:4F:4F:04',
        '4E:53:50:4F:4F:05',
        '4E:53:50:4F:4F:06',
        '4E:53:50:4F:4F:07',
        '4E:53:50:4F:4F:08',
        '4E:53:50:4F:4F:09',
        '4E:53:50:4F:4F:0A',
        '4E:53:50:4F:4F:0B',
        '4E:53:50:4F:4F:0C',
        '4E:53:50:4F:4F:0D',
        '4E:53:50:4F:4F:0E',
        '4E:53:50:4F:4F:0F',
        '4E:53:50:4F:4F:10',
        '4E:53:50:4F:4F:11',
        '4E:53:50:4F:4F:12',
        '4E:53:50:4F:4F:13',
        '4E:53:50:4F:4F:14',
        '4E:53:50:4F:4F:15',
        '4E:53:50:4F:4F:16',
        '4E:53:50:4F:4F:17',
        '4E:53:50:4F:4F:18',
        '4E:53:50:4F:4F:19',
        '4E:53:50:4F:4F:1A',
        '4E:53:50:4F:4F:1B',
        '4E:53:50:4F:4F:1C',
        '4E:53:50:4F:4F:1D',
        '4E:53:50:4F:4F:1E',
        '4E:53:50:4F:4F:1F',
        '4E:53:50:4F:4F:20',
        '4E:53:50:4F:4F:21',
        '4E:53:50:4F:4F:21',
        '4E:53:50:4F:4F:23',
        '4E:53:50:4F:4F:24',
        '4E:53:50:4F:4F:25',
        '4E:53:50:4F:4F:26',
        '4E:53:50:4F:4F:27',
        '4E:53:50:4F:4F:28',
        '4E:53:50:4F:4F:29',
        '4E:53:50:4F:4F:2A',
        '4E:53:50:4F:4F:2B',
        '4E:53:50:4F:4F:2C',
        '4E:53:50:4F:4F:2D',
        '4E:53:50:4F:4F:2E',
        '4E:53:50:4F:4F:2F',
        '4E:53:50:4F:4F:30',
        '4E:53:50:4F:4F:31',
        '4E:53:50:4F:4F:32',
        '4E:53:50:4F:4F:33',
        '4E:53:50:4F:4F:34',
        '4E:53:50:4F:4F:35',
        '4E:53:50:4F:4F:36',
        '4E:53:50:4F:4F:37',
        '4E:53:50:4F:4F:38',
        '4E:53:50:4F:4F:39',
        '4E:53:50:4F:4F:3A',
        '4E:53:50:4F:4F:3B',
        '4E:53:50:4F:4F:3C',
        '4E:53:50:4F:4F:3D',
        '4E:53:50:4F:4F:3E',
        '4E:53:50:4F:4F:3F',
        '4E:53:50:4F:4F:50',
        '4E:53:50:4F:4F:51',
        '4E:53:50:4F:4F:52',
        '4E:53:50:4F:4F:53',
        '4E:53:50:4F:4F:54',
        '4E:53:50:4F:4F:55',
        '4E:53:50:4F:4F:56',
        '4E:53:50:4F:4F:57',
        '4E:53:50:4F:4F:58',
        '4E:53:50:4F:4F:59',
        '4E:53:50:4F:4F:5A',
        '4E:53:50:4F:4F:5B',
        '4E:53:50:4F:4F:5C',
        '4E:53:50:4F:4F:5D',
        '4E:53:50:4F:4F:5E',
        '4E:53:50:4F:4F:5F',
        '4E:53:50:4F:4F:60',
        '4E:53:50:4F:4F:61',
        '4E:53:50:4F:4F:62',
        '4E:53:50:4F:4F:63',
        '4E:53:50:4F:4F:64',
        '4E:53:50:4F:4F:65',
        '4E:53:50:4F:4F:66',
        '4E:53:50:4F:4F:67',
        '4E:53:50:4F:4F:68',
        '4E:53:50:4F:4F:69',
        '4E:53:50:4F:4F:6A',
        '4E:53:50:4F:4F:6B',
        '4E:53:50:4F:4F:6C',
        '4E:53:50:4F:4F:6D',
        '4E:53:50:4F:4F:6E',
        '4E:53:50:4F:4F:6F',
        '4E:53:50:4F:4F:70',
        '4E:53:50:4F:4F:71',
        '4E:53:50:4F:4F:72',
        '4E:53:50:4F:4F:73',
        '4E:53:50:4F:4F:73',
        '4E:53:50:4F:4F:75',
        '4E:53:50:4F:4F:76',
        '4E:53:50:4F:4F:77',
        '4E:53:50:4F:4F:78',
        '4E:53:50:4F:4F:79',
        '4E:53:50:4F:4F:7A',
        '4E:53:50:4F:4F:7B',
        '4E:53:50:4F:4F:7C',
        '4E:53:50:4F:4F:7D',
        '4E:53:50:4F:4F:7E',
        '4E:53:50:4F:4F:7F',
        '4E:53:50:4F:4F:80',
        '4E:53:50:4F:4F:81',
        '4E:53:50:4F:4F:82',
        '4E:53:50:4F:4F:83',
        '4E:53:50:4F:4F:84',
        '4E:53:50:4F:4F:85',
        '4E:53:50:4F:4F:86',
        '4E:53:50:4F:4F:87',
        '4E:53:50:4F:4F:88',
        '4E:53:50:4F:4F:89',
        '4E:53:50:4F:4F:8A',
        '4E:53:50:4F:4F:8B',
        '4E:53:50:4F:4F:8C',
        '4E:53:50:4F:4F:8D',
        '4E:53:50:4F:4F:8E',
        '4E:53:50:4F:4F:8F',
        '4E:53:50:4F:4F:90',
        '4E:53:50:4F:4F:91',
        '4E:53:50:4F:4F:92',
        '4E:53:50:4F:4F:93',
        '4E:53:50:4F:4F:94',
        '4E:53:50:4F:4F:95',
        '4E:53:50:4F:4F:96',
        '4E:53:50:4F:4F:97',
        '4E:53:50:4F:4F:98',
        '4E:53:50:4F:4F:99',
        '4E:53:50:4F:4F:9A',
        '4E:53:50:4F:4F:9B',
        '4E:53:50:4F:4F:9C',
        '4E:53:50:4F:4F:9D',
        '4E:53:50:4F:4F:9E',
        '4E:53:50:4F:4F:9F',
        ]

        if options.shuffle:
                shuffle(addr)

        wait = 10

        print 'Initializing wireless interface'
        call(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-z'])
        call(['launchctl', 'unload', '-w', '/System/Library/LaunchDaemons/com.apple.InternetSharing.plist'])
        time.sleep(3)

        for a in addr:
                print 'Cycling WiFi...'
                call(['ifconfig', options.interface, 'lladdr', a])
                call(['launchctl', 'load', '-w', '/System/Library/LaunchDaemons/com.apple.InternetSharing.plist'])
                print 'Spoofing ' + options.interface + ' to ' + a + ' for 60 seconds'
                time.sleep(60)

                print 'Switching off sharing and waiting 3 seconds'
                call(['launchctl', 'unload', '-w', '/System/Library/LaunchDaemons/com.apple.InternetSharing.plist'])
                time.sleep(3)
        
                if options.pause:
                        wait -= 1
                        
                        if wait == 0:
                                print 'That\'s it, let me know if you need more StreetPassin\''
                                response = raw_input()
                                if response.isdigit():
                                        wait = int(response)
                                elif response == 'q':
                                        cleanup()
                                else:
                                        wait = 10
                                        
        print 'The list has been exhausted. Consider this HomePass session complete.'
        cleanup()
        
def cleanup():
        call(['launchctl', 'unload', '-w', '/System/Library/LaunchDaemons/com.apple.InternetSharing.plist'])
        print 'Finished'
        sys.exit()

if __name__ == "__main__":
        main(sys.argv[1:])
