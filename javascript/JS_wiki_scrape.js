// select all the tables using 'table' element
let table = document.querySelectorAll('table');
let headerTbl = table[1].querySelector('thead').querySelectorAll('th');
// loop through header and print all of the header names
let winnersObj = {}
let headerNames = [];
for (h in headerTbl) { 
    if (headerTbl[h].textContent === undefined) {
        continue
    }else{
    winnersObj[(headerTbl[h].textContent)] = [];
    headerNames.push(headerTbl[h].textContent);
    }
}
console.log(winnersObj);

let bodyTbl = table[1].querySelector('tbody').querySelectorAll('td');

let j = 0;
while (j < bodyTbl.length){
    let i = 0;
    while (i < Object.keys(winnersObj).length){
        winnersObj[headerNames[i]].push(bodyTbl[j].textContent);
        i++;
        j++;
    }
}

console.log(winnerObj)