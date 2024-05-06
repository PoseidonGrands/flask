;

var account_reg_opt = {
    init:function(){
        this.eventBind();
    },
    eventBind:function (){
        $(".reg_wrap .do-reg").click(function(){
            const login_name = $(".reg_wrap input[id=login_user]").val();
            const login_pwd = $(".reg_wrap input[id=login_pwd]").val();
            const repeat_pwd = $(".reg_wrap input[id=login_pwd_repeat]").val();

            const btn_submit = $(this);
            if(btn_submit.hasClass('disabled')){
                opsCommon.alert('请不要重复点击...');
                return;
            }

            // < 1的情况：输入空白字符
            if(login_name === undefined || login_name.length < 1){
                opsCommon.alert('请输入用户名');
                return;
            }
            if(login_pwd === undefined || login_pwd.length < 1){
                opsCommon.alert('请输入密码');
                return;
            }
            if(repeat_pwd === undefined || repeat_pwd.length < 1){
                opsCommon.alert('请再次输入密码');
                return;
            }

            btn_submit.addClass('disabled')
            $.ajax({
                url: opsCommon.buildUrl('/account/reg'),
                type: 'POST',
                data:{
                    login_name:login_name,
                    login_pwd:login_pwd,
                    repeat_pwd:repeat_pwd,
                },
                dataType: 'json',
                success: function (res){
                    //成功获得响应，按钮恢复点击
                    btn_submit.removeClass('disabled')
                    var callback = null
                    if(res.code === 200) {
                        callback = function () {
                            window.location.href = opsCommon.buildUrl('/')
                        }
                    }
                    opsCommon.alert(res.msg, callback)
                }
            })
        });
    }
}

$(document).ready(function(){
    account_reg_opt.init( )
});