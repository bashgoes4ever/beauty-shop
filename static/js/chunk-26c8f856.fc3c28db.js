(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-26c8f856"],{"0acd":function(t,e,a){},1265:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("section",{staticClass:"basket-page"},[a("div",{staticClass:"container"},[a("RouterLink",{staticClass:"back-link",attrs:{to:"/shop"}},[a("svg",{attrs:{viewBox:"0 0 12 10",fill:"none",xmlns:"http://www.w3.org/2000/svg"}},[a("path",{attrs:{d:"M0.833496 5.18197L10.8335 5.18197",stroke:"#22252C","stroke-width":"1.5","stroke-linecap":"round","stroke-linejoin":"round"}}),a("path",{attrs:{d:"M4.8667 9.19868L0.833365 5.18268L4.8667 1.16602",stroke:"#22252C","stroke-width":"1.5","stroke-linecap":"round","stroke-linejoin":"round"}})]),a("span",[t._v("Вернуться в магазин")])]),a("Basket")],1)])},s=[],i=a("26d5"),r={name:"BasketPage",components:{Basket:i["a"]}},o=r,c=a("2877"),l=Object(c["a"])(o,n,s,!1,null,"ba9d017c",null);e["default"]=l.exports},"26d5":function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"shop-basket"},[t._m(0),a("div",{staticClass:"total-price flex-between align-center"},[a("span",[t._v("Сумма заказа")]),a("div",{staticClass:"price"},[t._v(t._s(t.$store.getters.totalPrice)+" руб.")])]),a("div",{staticClass:"basket-content"},[a("img",{staticClass:"bg",attrs:{src:"/static/img/shop/1.png",alt:""}}),a("div",{staticClass:"basket-items"},t._l(t.$store.getters.basket,(function(t){return a("BasketItem",{key:t.id,attrs:{item:t}})})),1),a("Form")],1)])},s=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"head"},[a("span",[t._v("Корзина")])])}],i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{class:["basket-item flex-between align-end",{"basket-item-loading":t.loading}]},[a("div",{staticClass:"left"},[a("div",{staticClass:"title"},[t._v(t._s(t.item.product.name))]),a("QuantityInput",{on:{input:t.handleQuantityChange},model:{value:t.item.quantity,callback:function(e){t.$set(t.item,"quantity",e)},expression:"item.quantity"}})],1),a("div",{staticClass:"right"},[a("div",{staticClass:"price"},[t._v(t._s(t.item.product.price)+" руб.")]),a("div",{staticClass:"delete",on:{click:t.removeFromBasket}},[a("span",[t._v("Удалить")]),a("svg",{attrs:{viewBox:"0 0 12 14",fill:"none",xmlns:"http://www.w3.org/2000/svg"}},[a("path",{attrs:{d:"M8 0.333008H4C3.26467 0.333008 2.66667 0.931008 2.66667 1.66634V2.33301H0V3.66634H1.33333V12.333C1.33333 13.0683 1.93133 13.6663 2.66667 13.6663H9.33333C10.0687 13.6663 10.6667 13.0683 10.6667 12.333V3.66634H12V2.33301H9.33333V1.66634C9.33333 0.931008 8.73533 0.333008 8 0.333008ZM4 1.66634H8V2.33301H4V1.66634ZM9.33333 12.333H2.66667V3.66634H9.33333V12.333Z",fill:"#EB5757"}}),a("path",{attrs:{d:"M4 4.99967H5.33333V10.9997H4V4.99967Z",fill:"#EB5757"}}),a("path",{attrs:{d:"M6.66667 4.99967H8V10.9997H6.66667V4.99967Z",fill:"#EB5757"}})])])]),t.loading?a("Loader",{staticClass:"loader"}):t._e()],1)},r=[],o=a("1da1"),c=(a("96cf"),a("2ef0")),l=a.n(c),d=a("d4cb"),u=a("555f"),m={name:"BasketItem",components:{QuantityInput:d["a"],Loader:u["a"]},props:["item"],data:function(){return{loading:!1}},methods:{handleQuantityChange:l.a.debounce((function(t){this.$store.dispatch("changeProductQuantity",{productId:this.item.id,quantity:t})}),300),removeFromBasket:function(){var t=this;return Object(o["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t.loading=!0,e.next=3,t.$store.dispatch("removeProductFromBasket",t.item.id);case 3:return e.next=5,t.$store.dispatch("createNotification","Товар удален из корзины");case 5:t.loading=!1;case 6:case"end":return e.stop()}}),e)})))()}}},p=m,f=(a("c0b6"),a("2877")),h=Object(f["a"])(p,i,r,!1,null,"53a602d9",null),v=h.exports,b=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("form",{class:[{"form-loading":t.loading}]},[t.loading?a("Loader",{staticClass:"loader"}):t._e(),a("div",{staticClass:"title"},[t._v("Оформить заказ")]),a("Input",{attrs:{disabled:!t.$store.getters.totalProducts||t.loading,type:"text",name:"name",placeholder:"Екатерина",label:"Ваше имя"},model:{value:t.form.name,callback:function(e){t.$set(t.form,"name",e)},expression:"form.name"}}),a("Input",{attrs:{disabled:!t.$store.getters.totalProducts||t.loading,type:"text",name:"name",placeholder:"+7 999 999 99 99",label:"Ваш телефон",mask:"phone"},model:{value:t.form.phone,callback:function(e){t.$set(t.form,"phone",e)},expression:"form.phone"}}),a("Input",{attrs:{disabled:!t.$store.getters.totalProducts||t.loading,type:"email",name:"name",placeholder:"example@mail.ru",label:"ваш email"},model:{value:t.form.email,callback:function(e){t.$set(t.form,"email",e)},expression:"form.email"}}),a("button",{staticClass:"btn",attrs:{disabled:!t.$store.getters.totalProducts||t.loading||!t.isValid},on:{click:t.submit}},[t._v(" заказать ")])],1)},g=[],k=a("1270"),_={name:"Form",components:{Input:k["a"],Loader:u["a"]},computed:{isValid:function(){return!!this.form.phone}},data:function(){return{loading:!1,form:{name:"",phone:"",email:""}}},methods:{submit:function(){var t=this;return Object(o["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return t.loading=!0,e.next=3,t.$store.dispatch("submit",t.form);case 3:return e.next=5,t.$store.dispatch("createNotification","Заказ успешно создан. Мы свяжемся с вами в ближайшее время");case 5:return e.next=7,t.$store.dispatch("fetchBasket");case 7:t.clearForm(),t.loading=!1;case 9:case"end":return e.stop()}}),e)})))()},clearForm:function(){this.form={name:"",phone:"",email:""}}}},C=_,w=(a("cc6e"),Object(f["a"])(C,b,g,!1,null,"dfaddda6",null)),x=w.exports,$={name:"Basket",components:{BasketItem:v,Form:x},data:function(){return{products:[{id:1,name:"Loreal Elseve",quantity:2,price:2700}]}}},B=$,V=Object(f["a"])(B,n,s,!1,null,"1ce44bfb",null);e["a"]=V.exports},"555f":function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},s=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"loader-wrapper"},[a("div",{staticClass:"lds-facebook"},[a("div"),a("div"),a("div")])])}],i={name:"Loader"},r=i,o=(a("5b26"),a("2877")),c=Object(o["a"])(r,n,s,!1,null,"004e328a",null);e["a"]=c.exports},"5b26":function(t,e,a){"use strict";a("de59")},c0b6:function(t,e,a){"use strict";a("0acd")},cc6e:function(t,e,a){"use strict";a("dfcd")},de59:function(t,e,a){},dfcd:function(t,e,a){}}]);
//# sourceMappingURL=chunk-26c8f856.fc3c28db.js.map