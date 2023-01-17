class Car {
    #name;
    #color;
    #speed;
  
    constructor(name, color) {
      this.#name = name;
      this.#color = color; 
      this.speed = 100
    }
   reduceSpeed(){
    console.log(this.#speed)
   } 
}

let car=  new Car("kjh","black")
console.log(car.reduceSpeed())