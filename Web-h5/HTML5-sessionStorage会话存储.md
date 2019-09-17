#### HTML5 sessionStorage会话存储

- sessionStorage 是HTML5新增的一个会话存储对象，用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据

- 最小浏览器版本支持
	- IE8
	- Chrome 5

- 存储上限：大多数浏览器上限5M

- 属性
	- `length`：返回一个整数，表示存储在 sessionStorage 对象中的数据项(键值对)数量

- 方法
	- `key(index)`: 返回当前 `sessionStorage` 对象的第`index`序号的`key`名称。若没有返回`null`
	- `getitem(key)`: 返回键名`key`对应的值`value`若没有返回`null`
	- setitem(key,value): 该方法接受一个键名`key`和值`value`作为参数，将键值对添加到存储中；如果键名存在，则更新其对应的值(key、value都为string)
	- `removeItem(key)`: 将指定的键名`key`从 `sessionStorage` 对象中移除
	-  `clear()`: 清除 sessionStorage 对象所有的项

##### 小示例

- 存储数据
```javascript

// setitem() 方法
sessionStorage.setItem('testKey','testvalue'); // 存入一个值
// 属性方式
sessionStorage['testKey'] = 'testvalue'
```

- 读取

```javascript
// getItem()方法
sessionStorage.getItem('testKey'); // => 返回testKey对应的值 testvalue
// 属性方式获取
sessionStorage['testKey'];  // => testvalue
```

##### 存储json对象
> **sessionStorage也可存储Json对象：存储时，通过JSON.stringify()将对象转换为文本格式；读取时，通过JSON.parse()将文本转换回对象**

```javascript

var user = {
	name: '张三',
	age:18,
	gender:'男'
}

// 存储值：将对象转换为Json字符串
sessionStorage.setItem('user', JSON.stringify(user));
 
// 取值时：把获取到的Json字符串转换回对象
var userStr = sessionStorage.getItem('user');
user = JSON.parse(userStr);
console.log(user.name);   // => 张三
```
