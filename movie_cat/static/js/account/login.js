;

var account_login_ops = {
    init:function (){
        this.eventBind()
    },
    eventBind:function (){
        $(".login_wrap .do-login").click(function (){
            let loginBtn = $(this);
            if(loginBtn.hasClass('disabled')){
                opsCommon.alert('请不要重复点击！')
            }
            let loginName = $(".login_wrap input[id='login_user']").val();
            let loginPwd = $(".login_wrap input[id='login_pwd']").val();
            console.log(typeof(loginPwd), loginPwd.length)
            //undefined为没取到控件的值，<1则是取到了空值（用户没输入
            if(loginName.length < 3 || loginPwd.length < 3){
                opsCommon.alert('无效字段值');
            }

            loginBtn.addClass('disabled');
            $.ajax({
                url: opsCommon.buildUrl('/account/login'),
                type: 'POST',
                data: {
                    loginName: loginName,
                    loginPwd: loginPwd
                },
                dataType: 'json',
                success: function (res){
                    //成功获得响应，按钮恢复点击
                    loginBtn.removeClass('disabled')
                    var callback = null
                    if(res.code === 200) {
                        callback = function () {
                            // 将当前页面重定向
                            window.location.href = opsCommon.buildUrl('/')
                        }
                    }
                    opsCommon.alert(res.msg, callback)
                }
            })

        })
    }
}

$(document).ready(function (){
    account_login_ops.init()
})