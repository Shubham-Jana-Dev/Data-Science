function firtst_code(){
    var b = 90;
    console.log(b);
}
//firtst_code();

function second(){
    console.log(b); //undefined
    var b = 30;
}
//second();

function example3(){
    console.log(d);
    let d = 89;
}
//example3();

function example4(){
    console.log(u);
    const u = 90;
}
//example4();

function example_bolck_scope(){
    for(let i = 0; i < 10; i++){
        if(i == 8){
            let c = 39;
            console.log(c);
        }
        // If we try to access c here it will throw a ReferenceError: c is not define
    }
}
//example_bolck_scope();

function example_function_scope_for_var(){
    for(let i = 0; i < 45; i++){
        if(i === 34){
            var g = "Shubham Jana";
           
        }
        console.log(g); // It would not throw an error because var is not block scope it's function scope
    }
}
//example_bolck_scope_for_var();

var name = "Shubham Jana";

function example_global_scope(){
    for(let i = 0; i < 100; i++){
        console.log(name);
        if(i == 99){
            console.log("Hello everyone my name is ",name);
        }
    }
}
//example_global_scope(); // It shows that we can access the name in anywhere in the code because it has been declear in the glogal scope

