var Links = {
  SetColor:function(color){
    var alist = document.querySelectorAll('a');
    var i = 0;
    while(i < alist.length){
      console.log(alist[i])
      alist[i].style.color= color;
        i +=1;
    }
    //$('a').css('color', color); jQuery를이용하여 a를 바꿈
    //but 지금 따로 틀 설정되어있어서 잘안됨..
  }
}
var Body = {
  SetColor:function(color){
    document.querySelector('body').style.color = color;
  },
  SetBackgroundColor:function(color){
    document.querySelector('body').style.backgroundColor = color;
  }
}
function nightDayHandler(self){
    var target = document.querySelector('body')
    if(self.value ==='night' ){
      Body.SetBackgroundColor('black');
      Body.SetColor('white');
      self.value ='  day  ';
      Links.SetColor('powderblue');
    } else {
      Body.SetBackgroundColor('white');
      Body.SetColor('black');
      self.value ='night';
      Links.SetColor('blue');
    }
  }
