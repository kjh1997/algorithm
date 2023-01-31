// function testAsync(){
//     return new Promise((resolve,reject)=>{
//         //here our function should be implemented 
//         setTimeout(()=>{
//             console.log("Hello from inside the testAsync function");
//             resolve();
//         ;} , 5000
//         );
//     });
// }

// async function callerFun(){
//     console.log("Caller");
//     await testAsync();
//     console.log("After waiting");
// }

// callerFun();


class people{
    #name="";
    #age=0;
    constructor(name,age){
        this.#name = name
        this.#age = age
    }
    
    getName(){
        return this.#name
    }
    getAge(){
        return this.#age
    }

}

p = new people("kjh",25)
console.log(p.getAge())

