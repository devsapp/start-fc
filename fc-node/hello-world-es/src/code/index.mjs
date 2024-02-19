
export const handler = async (event, context) => {
  console.log("receive event: \n" + event);
  return "Hello World!";
};