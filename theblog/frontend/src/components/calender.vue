<template>

<div class="container">
<h1> vue calender</h1>
<h3>{{currentDayClass(5)}}</h3>
<h2>{{currentMonthName}} / {{currentYear}}</h2>
<h1>{{currentDate}}</h1>
<section >
<p v-for="day in days " :key="day">{{day}}</p>
</section>

<section >
<p v-for="day in startDay()" :key="day"></p>
</section>
<section >
<p v-for="num in  daysInMonth()" :key="num"
:class="currentDayClass(num)"
>{{num}}</p>
</section>
<section class="but">
<button class="but1" @click="prev">prev</button>
<button class="but2" @click="next">next</button>
</section>
</div>
</template>
<script>
export default{
data(){
return{
days:['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],
currentMonth:new Date().getMonth(),
currentMonthName:new Date().toLocaleString("default",{month:"long"}),
currentYear:new Date().getFullYear(),
currentDate:new Date().getUTCDate(),
}
},
methods:{
daysInMonth(){

return new Date(this.currentYear,this.currentMonth+1,0).getDate();
},
startDay(){
return new Date(this.currentYear,this.currentMonth, 1).getDay();
},
next(){
if(this.currentMonth==11){
this.currentYear++;
this.currentMonth=0;
}
else{
this.currentMonth++;}
},

prev(){
if(this.currentMonth==0){
this.currentYear--;
this.currentMonth=11;
}
else{
this.currentMonth--;}
},
currentDayClass(num){
const calenderFullDate=new Date(this.currentYear,this.currentMonth,num).toDateString();
const currentFullDate=new Date().toDateString();
return calenderFullDate==currentFullDate? 'highlight': ''

}
},
components:{},
computed:{
currentMonthName(){
return new Date(this.currentYear, this.currentMonth).toLocaleString("default",{month:"long"})
}
},

}
</script>

<style>
.container{
text-align:center;
}
section {
display:flex;
justify-content:center;
}

h1{
padding:10px;
font-family: Inter bold;
font-weight: bold;

}
section p{
margin:10px;
}

.but{
display:flex;
margin:20px;}

.but .but1{
margin-right:100px;
background-color:#654321;
padding-left:15px;
padding-right:15px;
color:#FFFFFF;
}
.but .but2{
background-color:#654321;
padding-left:15px;
padding-right:15px;
margin-left:100px;
color:#FFFFFF;
}
.highlight{
color:#654321;}
</style>