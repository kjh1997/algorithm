const axios = require('axios')

// const test = new Promise((resolve, reject)=>{
//     setTimeout(()=>{
//       reject("reject");
//     }, 3000);
//   });
  
//   test.then(result => console.log(result))
//   .catch(error => console.log("tes" + error));

axios.get("www.naver.com",{})
.then(()=>{console.log("fadfadsf")})
.catch(()=> {console.log("finish")})

const a = "test"
a = "test2"
console.log(a)
