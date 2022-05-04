<template>

<div class="container">


<h1 class="text-center">____________ letters <span>{{count}}</span>___________</h1>

<ul>
<li v-for="(value,index) in let " :key="value.l">

<div> {{ value.l}} <button v-on:click="remove(index)">X </button ></div>
<input />

 </li>


</ul>

<form @submit.prevent="add" class="form">
<textarea v-model="name" ></textarea>

<br>
<button type="submit" class="border rounded bg-gradient-to-t from-red-700 to-green-500" > add </button>
<br>

</form>

</div>
</template>
<script>


export default{





computed:{


count(){
return this.let.length + ' letters'},


},

methods:{
add(){
if(this.name != ''){
    this.let.unshift({ l : this.name });
    this.name='';}
},

remove(key){
this.let=this.let.filter((value,i)=>i !=key);

}



},



data(){
return{
let:[{l:'r'},{l:'a'},{l:'b'},{l:'a'},{l:'b'}],
name:"rabab",
isDisabled: true,

}}
}
</script>

<style>
.container{
text-align:center;
margin:10px;
background-color:#FFFFFF;

}
.span{
color:green;
}
.ul{
justify-text:center;
},
.form textarea{
border:#654321;}
.form button{
background-color:#654321;
padding-left:15px;
padding-right:15px;
}
</style>