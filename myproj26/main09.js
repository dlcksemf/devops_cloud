const get_default_value = () => {
    console.log("get_default_value() 함수 호출")
    return 10;
};

function hello(name, age=get_default_value()) {
    console.log(`안녕. 난 ${name}이야. ${age}살이지.`);
}

hello("Tom");
hello("Steve");
hello("John");