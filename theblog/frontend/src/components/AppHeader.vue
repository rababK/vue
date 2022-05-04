<template>
<p class="header">
<router-link class="item" v-for="item in list" :key="item.to" :to="item.to"> {{item.title}} </router-link>

</p>
</template>


<script>
export default{
data(){
return{
list:[
{title:"HOME",to:"/"},
{title:"LETTERS",to:"/letters"},
{title:"CALENDER",to:"/calender"},
{title:"MARKDOWN",to:"/markdown"},
]}
}
}
</script>
<style>
.header{
background-color:#654321;
padding:20px;
margin :20px;

}
.item{
margin :20px;
}
</style>