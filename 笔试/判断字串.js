function includes( s1 ,  s2 ) {
  // write code here
  if (s2 === ''){
    return true;
  } else if (s1 === ''){
    return false;
  }
  let a = s1.split('')
  let b = s2.split('');
  
  const fn = (a, b) => {
      for (let i = 0; i < a.length; i++) {
          if (a[i] === b[0]) {
              b.shift();
          }
      }
      return b.length === 0;
  }
  
  return fn(a, b.slice()) || fn(a, b.reverse().slice());
}


const s1 = "arash", s2 = "aaa"
console.log(includes(s1, s2));