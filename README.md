Trunk Player
============

Python Django web frontend for playing recorded radio transmisisons. The audio files are recorded using [Trunk Recoder](https://github.com/robotastic/trunk-recorder).

# WIP
### This is a forked version of ScanOC's Trunk-Player repo. There are numerous changes within this project that will likely not function on your machine.


## Quick Notes on this repo...
1. Encoded mp3 files will end up in your root OS directory: `/trunk-player-audio/`. Hint: It's expecting that folder to be mounted on spinning rust.
2. Some admin pages (htmls and alert sections) utilize CKEditor.
3. This repo has nearly ALL static files (excluding mp3's) on the AWS S3 CDN. 
4. There are some hard coded URL's currently to said CDN - will fix those up soon.
5. Numerous python packages have been updated as far as possible without breaking TrunkPlayer completely. This includes most security fixes.
6. Installation of this particular fork may be troublesome.

## Build and Install
  Documents are at Read the Docs [http://trunk-player.readthedocs.io/](http://trunk-player.readthedocs.io/)

## Support
 There is a google groups mailing list [Trunk Player](https://groups.google.com/forum/#!forum/trunk-player)

## Using with Unitrunker/EDACS Systems
 Check out https://github.com/MaxwellDPS/Unibridge for using Trunk-Player with unitrunker

## License
 Trunk Player is licensed under the [MIT License](License.txt)
