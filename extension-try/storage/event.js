chrome.storage.onChanged.addListener(function(changes,areaName) {
    console.log(changes);
});

chrome.storage.sync.set({"color":"balck","color2":"yello"},function() {});

chrome.storage.sync.set({"color":"black","color2":"yellow"},function() {});