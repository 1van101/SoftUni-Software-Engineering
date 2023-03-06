function solve(arr){
    let dictionary = {}

    for (const iterator of arr) {
        let currObject = JSON.parse(iterator);
        let key = Object.keys(currObject)[0];
        let value = Object.values(currObject)[0]
        
        dictionary[key] = value;
    }

    let dictKeys = Object.keys(dictionary).sort()

    for (const key of dictKeys) {
        console.log(`Term: ${key} => Definition: ${dictionary[key]}`);
    }
}


solve([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]
    )