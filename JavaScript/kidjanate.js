// Useage `node JavaScript/kidjanate.js` or run from web browser.

function GetCodeOrKofi()
{
    let Coffee = "Coffee";
    let Code = ""
    for (let i = 0; i < Coffee.length; i++) {
        if (Code.length == 0) {Code+=Coffee[i];}else{
            let chrToAdd = "";
            if (Code[Code.length-1].charCodeAt(0) == 111)
            {
                chrToAdd = String.fromCharCode(100);
            }
            else
            {
                chrToAdd = Coffee[i];
            }
            Code+=chrToAdd;
        }
    }
    return Code.substr(0,3) + Code[5];
}

console.log(GetCodeOrKofi());