"use strict";

var throwProperUsageException = function() {
    throw new Error("improper usage\nproper usage:\n    grep <STRING> <FILE>\n    wc <FILE>\n    grep <STRING> <FILE> | wc");
};

var command;
var grepString;
var fileName;
const args = process.argv;

//CHECK FOR PROPER USAGE
(function () {
    var numberOfArgs = args.length;
    switch(numberOfArgs) {
        case 4:
            if (args[2].toLowerCase() !== "wc") {
                throwProperUsageException();
            }
            command = "WC";
            fileName = args[3];
            break;
        case 5:
            if (args[2].toLowerCase() !== "grep") {
                throwProperUsageException();
            }
            command = "GREP";
            grepString = args[3];
            fileName = args[4];
            break;
        case 7:
            if (args[2].toLowerCase() !== "grep"
                || args[5] !== "|"
                || args[6] !== "wc") {
                throwProperUsageException();
            }
            command = "GREPWC";
            grepString = args[3];
            fileName = args[4];
            break;
        default:
            throwProperUsageException();
    }
}());

//got following code from: https://code-maven.com/reading-a-file-with-nodejs
var fs = require("fs");
var fileContents = fs.readFileSync(fileName, "utf8");
var lines = fileContents.split(/\r?\n/);

if (command.includes("GREP")) {
    lines = lines.filter((line) => line.includes(grepString));
} if (command.includes("WC")) {
    lines.map((line) => line.toLowerCase()) //convert-case
        .flatMap((line) => line.split(" ")) //find-words
        .map((word) => word.replace(/[^a-zA-Z0-9]+/g, "").trim()) //nonABCfilter - remove nonAlphaNumeric
        .filter((word) => word !== "") //nonABCfilter - remove white space words
        .reduce(function(accumulator, word) {
            if(! (accumulator instanceof Map)) {
                var firstWord = accumulator;
                accumulator = new Map();
                accumulator.set(firstWord, 1);
            }
            var count = accumulator.get(word);
            accumulator.set(word, count === undefined ? 1 : count + 1);
            return accumulator;})
        .forEach((count, word) => console.log(word + " - " + count));
}
if (command === "GREP") {
    lines.forEach((line) => console.log(line));
}