for(i = 0; i < 5; i++){
    let row = [];
    for(j = 0; j < 5; j++){
        if(i % 2 == 0){
            if(j % 2 == 0){
                row.push(0);
            }else{
                row.push(1);
            }
        }else{
            if(j % 2 == 0){
                row.push(1);
            }else{
                row.push(0);
            }
        }
    }
    console.log(row.join(" "));
}