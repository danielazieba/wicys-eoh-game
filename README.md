# WiCyS: EOH 2021 JavaScript edition

## About

Some members of the Women in Cybersecurity chapter at UIUC came together to work on a project for Engineering Open House 2021, an annual UIUC event seeking to highlight its College of Engineering, especially for middle and high school attendees. We thought a game would be more interactive than the expectation of EOH exhibits being pre-recorded video activities, so we threw this together. Give it a try if you want to work on some beginner-friendly CTF-ish problems!

## Things you need

- Node.js
- HTTP server (needs to be downloaded; it's a Node.js package https://www.npmjs.com/package/http-server)
- The code in this repo

## How to run

Get into the top-level directory of this repo (ie. wherever this README is located) and start up your http-server. You should just need to type ```http-server``` and it should spawn a basic HTTP server. Then, open up ```localhost:8080```, where you should see a basic list of files in the directory where you started the server, and click files until you open ```eoh-game.html```, at which point the game should be running.

## How to work on this

This is built on ga.js, a basic game engine. If you have questions about built-in functions for that, see https://github.com/kittykatattack/ga. 
