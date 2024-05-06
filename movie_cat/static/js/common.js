;

var domain = 'http://127.0.0.1:5002'
const opsCommon = {
    buildUrl: function (path, params) {
        var paramsUrl = "";
        if( params ){
            //Object.keys(params)取出params的全部键
            //.map(function(k){})对每个键进行函数操作
            paramsUrl = Object.keys(params).map(function (k){
                // 列表中两个元素通过join链接后变成字符串，如{name:sewell he, age:25, sex:'男'}取出键是[name, age, sex]
                // map函数对第一项操作后变成: name=sewell%20he
                //新列表结果存储在paramsUrl
                return [ encodeURIComponent(k), encodeURIComponent( params[k] ) ].join('=')
            }).join('&');
            paramsUrl = '?' + paramsUrl;
        }

        return path + paramsUrl;
    },
    alert:function(msg, cb){
        layer.alert(msg, {
            //点击确认（值是yes）调用函数
            yes:function(index){
                //传入的cb确实是回调函数
                if(typeof cb == "function"){
                    cb()
                }
                layer.close(index)
            }
        })
    }
};

