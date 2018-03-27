var socket;

$(function () {
    socket = io();

    socket.emit('set client');

    //--- Update html with data from server --- //
    socket.on('rfidEvent', function (msg) {
        // console.log(msg);
        $('#videoFrame').html(msg);
    });

});