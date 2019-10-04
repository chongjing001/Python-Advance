var username = document.cookie.split(";")[0].split("=")[1];
//JS操作cookies方法!
//写cookies
function setCookie(name, value) {
    var Days = 365;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
}

function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}


//加密方法
//data: 需要加密的数据
//token: 用户的token
function enAES(data = {}, token) {
    let str = JSON.stringify(data)
    let key = token.substring(0, 16)
    var encrypt = CryptoJS.AES.encrypt(str, CryptoJS.enc.Utf8.parse(key), {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypt.toString();
}

//通用ajax函数
//固定使用POST访问
//url: 接口地址
//data: 需要传输的数据
//success: 成功回调函数
function POST(url, data = {}, success = function () {
}, error = function () {
}) {
    let csrftoken = getCookie('csrftoken');
    axios({
        url: url,
        method: 'post',
        data: data,
        headers: {"X-CSRFToken": csrftoken},
        transformRequest: [function (data) {
            return Qs.stringify(data)
        }]
    }).then(success).catch(error);
}

function GET(url, data = {}, success = function () {
}, error = function () {
}) {
    axios.get(url, {
        'params': data,
        //如果出现特定中文字符编码出错，可以试试取消注释以下代码
        //'transformRequest': [function(data){
        //    return Qs.stringify(data)
        //}]
    }).then(success).catch(error);
}

function PUT(url, data = {}, success = function () {
}, error = function () {
}) {
    let csrftoken = getCookie('csrftoken');
    axios({
        url: url,
        method: 'put',
        data: data,
        headers: {"X-CSRFToken": csrftoken},
        transformRequest: [function (data) {
            return Qs.stringify(data)
        }]
    }).then(success).catch(error);
}

function DELETE(url, data = {}, success = function () {
}, error = function () {
}) {
    let csrftoken = getCookie('csrftoken');
    axios({
        url: url,
        method: 'delete',
        data: data,
        headers: {"X-CSRFToken": csrftoken},
        transformRequest: [function (data) {
            return Qs.stringify(data)
        }]
    }).then(success).catch(error);
}

//字符串格式化函数
//第一个参数：被格式化的字符串
//例如"<div>{0}</div>"
//第二个及后面的所有参数为需要格式化进去的字符串
//后面参数的顺序与前面一致
//例如：
//text1 = '<div>{0}</div><span>{1}</span><label>{2}</label>'
//StringFormat(text1, '今天', '天气', '真好')
//结果为：
//<div>今天</div><span>天气</span><label>真好</label>
//函数未做合法性校验，所以注意一下自己传的数据有没有问题
function StringFormat() {
    if (arguments.length == 0) return null;
    var str = arguments[0];
    for (var i = 1; i < arguments.length; i++) {
        var re = new RegExp('\\{' + (i - 1) + '\\}', 'gm');
        str = str.replace(re, arguments[i]);
    }
    return str;
}

//废弃
//function showMsg(text){
//	var type = 'auto'
//
//	layer.open({
//		type: 1
//		,offset: type
//		,id: 'layerDemo'+type
//		,content: '<div style="padding: 20px 100px;">'+ text +'</div>'
//		,btn: '确定'
//		,btnAlign: 'c'
//		,shade: 0
//		,yes: function(){
//			layer.closeAll();
//		}
//	});
//}


function stringify(data) {
    if (typeof data === 'object') {
        let param = new URLSearchParams()
        for (var i in data) {
            let item = data[i]
            param.append(i, item)
        }
        return param
    } else {
        console.err("data需要是object对象")
        return
    }
}
