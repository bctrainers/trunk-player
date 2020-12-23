Trunk Player
============

Python Django web frontend for playing recorded radio transmisisons. The audio files are recorded using [Trunk Recoder](https://github.com/robotastic/trunk-recorder).

# WIP
**This is a forked version of ScanOC's Trunk-Player repo. There are numerous changes within this project that will likely not function on your machine due to non-confirming changes applied that were added after installation.**


### Quick Notes and differences from the main repo to this one...
1. Encoded mp3 files will end up in your root OS directory: `/trunk-player-audio/`. 
   * Hint: It's expecting that folder to be mounted on spinning rust, on its own unique drive. 
   * Ensure huge amounts of inodes are available. 
   * Do not dump all mp3's to the folder - use sub-folders. Linux has a hard time once you surpass 5 million files in a single directory. I learned that the hard way when i accessed it for the first time at 13 million mp3 files in a single folder. :-)
2. Some admin pages (web htmls and site alert sections) utilize CKEditor.
3. This repo has nearly ALL static files (excluding mp3's) on the AWS S3 CDN. That includes CSS, images, font-awesome, and javascript.
4. There are some hard coded URL's currently - will fix those soon.
5. Numerous python packages have been updated as far as possible without breaking TrunkPlayer completely. This includes most security fixes.
6. trunkplayer.css was set to be in dark mode.
7. Scanlist rows are persistently highlighted in red when a unit pokes their emergency button.
8. Single unit searching is functional on the front-end. Allowing you to view what radio ID has been on whatever talk groups.
9. Scanlists show three options when logged in as an admin: L A and T. 
   * L: Solo the radio ID to see all talk groups its been active on.
   * A: Access the admin page for said radio ID.
   * T: Inline assign a radio ID tag and type of radio.
10. Installation of this particular fork may be troublesome.
11. This fork assumes you're going to be running TrunkRecorder on a P25 system, no analog.
12. The wav to mp3 conversion...
   * Uses the ffmpeg package.
   * Intentionally converts the wave to a 24kbps mp3 file. (Yes, I am aware that 24kbps is overkill, but going anything less - you can hear the reduction in quality)
   * The audio spectrum is hard-capped at 8000hz, anything over it is clipped off/brick walled.

## Build and Install
  Documents are at Read the Docs [http://trunk-player.readthedocs.io/](http://trunk-player.readthedocs.io/)

## Support
 If you wish to install this particular fork and need assistance due to an install mishap or something else, please open an issue on this forked project.

## License
 Trunk Player is licensed under the [MIT License](License.txt)
