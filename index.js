const linebot = require('linebot');
const express = require('express');

const bot = linebot({
	channelId: process.env.1544752780,
	channelSecret: process.env.975d4c8d9ee2cb8da4a9cc06d40133df,
	channelAccessToken: process.env.L/0Npk/IntIGOiYL2m/mrwiuEO6H+Q5aAdQSsuougCLNS0qjI6OzqyJXFZ8bwT/pH26pg6YntaSJzKZ6Z8t7CCZ0tLkKHU2VOpaHprz3Va9ndGCx7tcMbiAU8goDK/ZMT1yyPk40JtLcJoc/2HGl9AdB04t89/1O/w1cDnyilFU=
});

const app = express();

const linebotParser = bot.parser();

app.get('/',function(req,res){
    res.send('Hello World!');
});

app.post('/linewebhook', linebotParser);

bot.on('message', function (event) {
	event.reply(event.message.text).then(function (data) {
		console.log('Success', data);
	}).catch(function (error) {
		console.log('Error', error);
	});
});

app.listen(process.env.PORT || 80, function () {
	console.log('LineBot is running.');
});
