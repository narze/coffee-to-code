const express=require('express');
const app =express();


app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));
app.use(express.urlencoded({extended:false}));

app.get('/',(req,res)=>{
    res.render('index',{'Code':0});
})


app.post('/',(req,res)=>{
    try{
        CoffeeString=req.body.coffee
        CodeString=CoffeeString.replaceAll(/coffee/ig,'Code')
        res.render('index',{'Code':CodeString});
    }
    catch{
        res.redirect('/');
    }
    
})

app.listen(3000,()=>console.log("App is Running at Port 3000"));