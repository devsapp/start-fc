'use strict';
/*
To enable the initializer feature (https://help.aliyun.com/zh/fc/user-guide/lifecycle-hooks-for-function-instances)
please implement the initializer function as below：
export const initializer = async (context) => {
  console.log('initializing');
  return "ok";
};
*/

export const handler = async (event, context) => {
  console.log("EVENT: \n" + event);
  return "Hello World!";
};