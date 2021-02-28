#!/usr/local/bin/python3

import minecraft_launcher_lib as mll
import subprocess

# Minecraft version
mc_version = "1.12.2"

# Asset index is same but without final revision
asset_index = "1.12"

# Your email, username and password below
login    = "yourEmailUsername"
password = "seekritPasswordHere"

# Get Minecraft directory
mc_directory = mll.utils.get_minecraft_directory()

libdir = mc_directory + "/libraries/"

lwjgl2_libs = '/usr/local/share/lwjgl/lwjgl.jar' \
  + ':/usr/local/share/lwjgl/lwjgl_util.jar' \
  + ':/usr/local/share/lwjgl/jinput.jar:'

# Make sure the desired version of Minecraft is installed
print("Installing version " + mc_version + " if needed... ", end='')
mll.install.install_minecraft_version(mc_version,mc_directory)
print("Done")

# Login
print("Logging in... ", end='')
login_data = mll.account.login_user( login, password )
print("Done")

# Useful figuring out new minecraft versions

#Get Minecraft command
#options = {
#    "username": login_data["selectedProfile"]["name"],
#    "uuid": login_data["selectedProfile"]["id"],
#    "token": login_data["accessToken"]
#}
#minecraft_command = mll.command.get_minecraft_command(mc_version,mc_directory,options)

#print(minecraft_command)

username = login_data["selectedProfile"]["name"]
uuid     = login_data["selectedProfile"]["id"]
token    = login_data["accessToken"]

real_command = ['/usr/local/jdk-11/bin/java',
  '-Djava.library.path=/usr/local/share/lwjgl/',
  '-Xms1G',
  '-Xmx2G',
  '-XX:-UseAdaptiveSizePolicy',
  '-Xmn256M',
  '-cp',
  libdir + 'com/mojang/patchy/1.1/patchy-1.1.jar:'
  + libdir + 'oshi-project/oshi-core/1.1/oshi-core-1.1.jar:'
  + libdir + 'net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar:'
  + libdir + 'net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar:'
  + libdir + 'com/ibm/icu/icu4j-core-mojang/51.2/icu4j-core-mojang-51.2.jar:'
  + libdir + 'net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar:'
  + libdir + 'com/paulscode/codecjorbis/20101023/codecjorbis-20101023.jar:'
  + libdir + 'com/paulscode/codecwav/20101023/codecwav-20101023.jar:'
  + libdir + 'com/paulscode/libraryjavasound/20101123/libraryjavasound-20101123.jar:'
  + libdir + 'com/paulscode/librarylwjglopenal/20100824/librarylwjglopenal-20100824.jar:'
  + libdir + 'com/paulscode/soundsystem/20120107/soundsystem-20120107.jar:'
  + libdir + 'io/netty/netty-all/4.1.9.Final/netty-all-4.1.9.Final.jar:'
  + libdir + 'com/google/guava/guava/21.0/guava-21.0.jar:'
  + libdir + 'org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar:'
  + libdir + 'commons-io/commons-io/2.5/commons-io-2.5.jar:'
  + libdir + 'commons-codec/commons-codec/1.10/commons-codec-1.10.jar:'
  + libdir + 'net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar:'
  + libdir + 'net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar:'
  + libdir + 'com/google/code/gson/gson/2.8.0/gson-2.8.0.jar:'
  + libdir + 'com/mojang/authlib/1.5.25/authlib-1.5.25.jar:'
  + libdir + 'com/mojang/realms/1.10.22/realms-1.10.22.jar:'
  + libdir + 'org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar:'
  + libdir + 'org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar:'
  + libdir + 'commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:'
  + libdir + 'org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar:'
  + libdir + 'it/unimi/dsi/fastutil/7.1.0/fastutil-7.1.0.jar:'
  + libdir + 'org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar:'
  + libdir + 'org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar:'
  + libdir + 'com/mojang/text2speech/1.10.3/text2speech-1.10.3.jar:'
  + lwjgl2_libs
  + mc_directory + '/versions/' + mc_version + '/' + mc_version + '.jar',
  'net.minecraft.client.main.Main',
  '--username', username,
  '--version', mc_version,
  '--gameDir', mc_directory,
  '--assetsDir', mc_directory + '/assets',
  '--assetIndex', asset_index,
  '--uuid', uuid,
  '--accessToken', token,
  '--userType', 'mojang',
  '--versionType', 'release'
]

# Start Minecraft
subprocess.call(real_command)
