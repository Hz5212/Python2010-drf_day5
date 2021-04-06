<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    注册
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">用户名:</td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="username" v-model="name" @blur="check_username"/>
                            <span id="username_msg" style="color: red"></span>
                        </td>

                    </tr>
                    <tr>
                        <td valign="middle" align="right">真实姓名:</td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="real_name"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">密码:</td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="password" @blur="check_password"/>
                            <span id="password_msg" style="color: red"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">确认密码:</td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="re_pwd" v-model="re_pwd" @blur="check_re_password"/>
                            <span id="re_password_msg" style="color: red"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">性别:</td>
                        <td valign="middle" align="left">
                            男
                            <input @click="gender=0" type="radio" class="inputgri" name="sex" value="m"
                                   checked="checked"/>
                            女
                            <input @click="gender=1" type="radio" class="inputgri" name="sex" value="f"/>
                        </td>
                    </tr>

                </table>
                <p>
                    <input type="submit" class="button" value="注册" @click="user_register"/>
                    <router-link to="/login">&nabla;登录</router-link>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Register",
    data() {
        return {
            name: "",
            real_name: "",
            password: "",
            re_pwd: "",
            gender: 0,
        }
    },
    methods: {
        check_username() {
            //获取输入的用户名
            let username = this.name
            //格式判断
            let pat = /^[a-zA-Z0-9_-]{2,16}$/
            //获取标签
            let span = document.getElementById("username_msg")
            //判断用户名是否为空
            if (username == null || username == "") {
                span.innerHTML = "用户名不能为空~~"
            }
            //验证格式
            else if (pat.test(username) == false) {
                span.innerHTML = "用户名格式不正确~~"
            } else {
                span.innerHTML = ""
            }
        },
        check_password() {
            //获取输入的密码
            let check_password = this.password
            //格式判断
            let pat = /^[a-zA-Z][a-zA-Z0-9\_\.\@\!\#\$\%\^\&\*\(\)]{6,16}/
            //获取标签
            let span = document.getElementById("password_msg")
            //判断密码是否为空
            if (check_password == null || check_password == "") {
                span.innerHTML = "密码不能为空~~"
            }
            //验证格式
            else if (pat.test(check_password) == false) {
                span.innerHTML = "密码强度不够~~"
            } else {
                span.innerHTML = ""
            }
        },
        check_re_password(){
            //获取输入数据
            let check_re_password = this.re_pwd
            //获取输入的密码
            let password = this.password
            //获取标签
            let span = document.getElementById("re_password_msg")
            //判断是否为空
            if(check_re_password==null||check_re_password == ""){
                span.innerHTML = "输入不能为空~~"
            }
            else if(check_re_password != password){
                span.innerHTML = "两次输入密码不匹配~~"
            }
            else {
                span.innerHTML = ""
            }
        },

        user_register() {
            // 向后端发送请求进行用户注册
            this.$axios({
                url: "http://127.0.0.1:8000/api/users/",
                method: "post",
                data: {
                    name: this.name,
                    real_name: this.real_name,
                    password: this.password,
                    re_pwd: this.re_pwd,
                    gender: this.gender,
                }
            }).then(res => {
                console.log(res.data);
                this.$message({
                    message: "恭喜您注册成功",
                    type: "success",
                    duration: 1000,
                    showClose: true
                })
                // 如果注册成功，则自动跳转到登录页
                this.$router.push("/login");

            }).catch(error => {
                console.log(error);
                this.$message.error("您提交的信息有误，请修改后提交~")
            })
        },
    }
}
</script>

<style scoped>

</style>
