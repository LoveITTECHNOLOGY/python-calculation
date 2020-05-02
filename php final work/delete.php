<?php
/**
 * Created by PhpStorm.
 * User: administer
 * Date: 2020/3/12
 * Time: 13:54
 */
//开始连接数据库
$conn=mysql_connect("localhost","root","");
//开始连接数据库表
mysql_select_db("mybook",$conn);
//开始将内容转换为中文字符
mysql_query("set names UTF8");
$id=intval($_GET["id"]);
echo $id;

$sql="delete from user where numer=$id";
if(mysql_query($sql)&&mysql_affected_rows()==1)
    echo "<script>alert('删除成功！');
location.href='index_1.php'</script>";
else
    echo "<script>alert('删除失败!');
    location.href='index_1.php'</script>";

?>
