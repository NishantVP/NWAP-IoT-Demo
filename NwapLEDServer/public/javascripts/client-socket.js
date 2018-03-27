var socket;

$(function () {
    socket = io();

    socket.emit('set client');

    //--- Update html with data from server --- //
    socket.on('stateChangeEvent', function (msg) {
        // console.log(msg);
        $('#stateText').html(msg);
    });

});