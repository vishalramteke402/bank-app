<!DOCTYPE html>
<!-- saved from url=(0073)https://colab.research.google.com/drive/1pxBWnZLey56FSawqJcg4Kqa3xBBmzj-N -->
<html lang="en" theme="dark" editor="Default Dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="vishalramteke402@gmail.com"><script type="text/javascript" async="" charset="utf-8" src="./bankapp_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-Kq9ivHFJO8Z7BQqPEcvZtkysKmz4eso0Q+Ti6hot0gaGWhIQRtinGXJKTesM5MuL" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./bankapp_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-Kq9ivHFJO8Z7BQqPEcvZtkysKmz4eso0Q+Ti6hot0gaGWhIQRtinGXJKTesM5MuL" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./bankapp_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-Kq9ivHFJO8Z7BQqPEcvZtkysKmz4eso0Q+Ti6hot0gaGWhIQRtinGXJKTesM5MuL" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./bankapp_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-Kq9ivHFJO8Z7BQqPEcvZtkysKmz4eso0Q+Ti6hot0gaGWhIQRtinGXJKTesM5MuL" nonce=""></script><script src="./bankapp_files/cb=gapi.loaded_1" nonce="" async=""></script><script type="text/javascript" async="" src="./bankapp_files/js" nonce=""></script><script src="./bankapp_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./bankapp_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>bank.ipynb - Colab</title><link href="./bankapp_files/css2" rel="stylesheet"><link href="./bankapp_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_4d{font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Qa:hover::after,a.gb_Qa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Qa:hover,a.gb_Qa:focus{text-decoration:none}a.gb_Qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Ra{background-color:#4285f4;color:#fff}a.gb_Ra:active{background-color:#0043b2}.gb_Sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Qa,.gb_Ra,.gb_Ta,.gb_Ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ta{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ua{background:#f8f8f8}.gb_Ta,#gb a.gb_Ta.gb_Ta,.gb_Ua{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ua{cursor:default;text-decoration:none}.gb_Ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ua{color:#fff}.gb_Ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Va{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Va:active,#gb .gb_Va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Va.gb_H{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Va.gb_H:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Va.gb_H:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Va.gb_H:active,#gb .gb_Va.gb_H:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_dd{display:inline-block;vertical-align:middle}.gb_Qe .gb_Q{bottom:-3px;right:-5px}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}.gb_ed{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_fd{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_fd{border-bottom-color:#ccc}.gb_la{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_dd.gb_Uc .gb_ed,.gb_dd.gb_Uc .gb_fd,.gb_dd.gb_Uc .gb_la,.gb_Uc.gb_la{display:block}.gb_dd.gb_Uc.gb_gd .gb_ed,.gb_dd.gb_Uc.gb_gd .gb_fd{display:none}.gb_Re{position:absolute;right:8px;top:62px;z-index:-1}.gb_hd .gb_ed,.gb_hd .gb_fd,.gb_hd .gb_la{margin-top:-10px}.gb_dd:first-child,#gbsfw:first-child+.gb_dd{padding-left:4px}.gb_Fa.gb_Se .gb_dd:first-child{padding-left:0}.gb_Te{position:relative}.gb_3c .gb_Te,.gb_Kd .gb_Te{float:right}.gb_B{padding:8px;cursor:pointer}.gb_B::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Fa .gb_id:not(.gb_Qa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_jd button svg,.gb_B{-webkit-border-radius:50%;border-radius:50%}.gb_jd button:focus:not(:focus-visible) svg,.gb_jd button:hover svg,.gb_jd button:active svg,.gb_B:focus:not(:focus-visible),.gb_B:hover,.gb_B:active,.gb_B[aria-expanded=true]{outline:none}.gb_Mc .gb_jd.gb_kd button:focus-visible svg,.gb_jd button:focus-visible svg,.gb_B:focus-visible{outline:1px solid #202124}.gb_Mc .gb_jd button:focus-visible svg,.gb_Mc .gb_B:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Mc .gb_jd.gb_kd button:focus-visible svg,.gb_jd button:focus-visible svg,.gb_Mc .gb_jd button:focus-visible svg{outline:1px solid currentcolor}}.gb_Mc .gb_jd.gb_kd button:focus svg,.gb_Mc .gb_jd.gb_kd button:focus:hover svg,.gb_jd button:focus svg,.gb_jd button:focus:hover svg,.gb_B:focus,.gb_B:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Mc .gb_jd.gb_kd button:active svg,.gb_jd button:active svg,.gb_B:active{background-color:rgba(60,64,67,.12)}.gb_Mc .gb_jd.gb_kd button:hover svg,.gb_jd button:hover svg,.gb_B:hover{background-color:rgba(60,64,67,.08)}.gb_Wa .gb_B.gb_Za:hover{background-color:transparent}.gb_B[aria-expanded=true],.gb_B:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_B[aria-expanded=true] .gb_F{fill:#5f6368;opacity:1}.gb_Mc .gb_jd button:hover svg,.gb_Mc .gb_B:hover{background-color:rgba(232,234,237,.08)}.gb_Mc .gb_jd button:focus svg,.gb_Mc .gb_jd button:focus:hover svg,.gb_Mc .gb_B:focus,.gb_Mc .gb_B:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Mc .gb_jd button:active svg,.gb_Mc .gb_B:active{background-color:rgba(232,234,237,.12)}.gb_Mc .gb_B[aria-expanded=true],.gb_Mc .gb_B:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Mc .gb_B[aria-expanded=true] .gb_F{fill:#fff;opacity:1}.gb_dd{padding:4px}.gb_Fa.gb_Se .gb_dd{padding:4px 2px}.gb_Fa.gb_Se .gb_z.gb_dd{padding-left:6px}.gb_la{z-index:991;line-height:normal}.gb_la.gb_ld{left:0;right:auto}@media (max-width:350px){.gb_la.gb_ld{left:0}}.gb_Ue .gb_la{top:56px}.gb_R{display:none!important}.gb_od{visibility:hidden}.gb_J .gb_B,.gb_ka .gb_J .gb_B{background-position:-64px -29px}.gb_1 .gb_J .gb_B{background-position:-29px -29px;opacity:1}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}@media screen and (max-width:319px){.gb_md:not(.gb_nd) .gb_J{display:none;visibility:hidden}}.gb_Q{display:none}.gb_ad{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_ad.gb_bd{color:#3c4043}.gb_Fa.gb_cc .gb_ad{margin-bottom:0}.gb_td.gb_vd .gb_ad{padding-left:4px}.gb_Fa.gb_cc .gb_wd{position:relative;top:-2px}.gb_cd{display:none}.gb_Fa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Fa.gb_Tc{min-width:120px}.gb_Fa.gb_xd .gb_yd{display:none}.gb_Fa.gb_xd .gb_md{height:56px}header.gb_Fa{display:block}.gb_Fa svg{fill:currentColor}.gb_Ed{position:fixed;top:0;width:100%}.gb_zd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Fd{height:64px}.gb_md{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Fa:not(.gb_cc) .gb_md{padding:8px}.gb_Fa.gb_Hd .gb_md{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa .gb_md.gb_nd.gb_Id{min-width:0}.gb_Fa.gb_cc .gb_md{padding:4px;padding-left:8px;min-width:0}.gb_yd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_Bd>.gb_yd{display:table-cell;width:100%}.gb_td{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa.gb_cc .gb_td{padding-right:14px}.gb_Cd{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Cd>:only-child{display:inline-block}.gb_Dd.gb_4c{padding-left:4px}.gb_Dd.gb_Jd,.gb_Fa.gb_Hd .gb_Dd,.gb_Fa.gb_cc:not(.gb_Kd) .gb_Dd{padding-left:0}.gb_Fa.gb_cc .gb_Dd.gb_Jd{padding-right:0}.gb_Fa.gb_cc .gb_Dd.gb_Jd .gb_Wa{margin-left:10px}.gb_4c{display:inline}.gb_Fa.gb_Xc .gb_Dd.gb_Ld,.gb_Fa.gb_Kd .gb_Dd.gb_Ld{padding-left:2px}.gb_ad{display:inline-block}.gb_Dd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Kd{height:48px}.gb_Fa.gb_Kd{min-width:auto}.gb_Kd .gb_Dd{float:right;padding-left:32px}.gb_Kd .gb_Dd.gb_Md{padding-left:0}.gb_Nd{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_qd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Od{color:black}.gb_Mc{color:white}.gb_Fa a,.gb_Qc a{color:inherit}.gb_ba{color:rgba(0,0,0,.87)}.gb_Fa svg,.gb_Qc svg,.gb_td .gb_ud,.gb_3c .gb_ud{color:#5f6368;opacity:1}.gb_Mc svg,.gb_Qc.gb_Vc svg,.gb_Mc .gb_td .gb_ud,.gb_Mc .gb_td .gb_Lc,.gb_Mc .gb_td .gb_wd,.gb_Qc.gb_Vc .gb_ud{color:rgba(255,255,255,.87)}.gb_Mc .gb_td .gb_Pd:not(.gb_Qd){opacity:.87}.gb_bd{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Mc .gb_bd,.gb_Od .gb_bd{opacity:1}.gb_Rd{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_X,span.gb_X{color:rgba(0,0,0,.87);text-decoration:none}.gb_Mc a.gb_X,.gb_Mc span.gb_X{color:white}a.gb_X:focus{outline-offset:2px}a.gb_X:hover{text-decoration:underline}.gb_Z{display:inline-block;padding-left:15px}.gb_Z .gb_X{display:inline-block;line-height:24px;vertical-align:middle}.gb_rd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Fa.gb_Kd .gb_rd{margin-left:8px}#gb a.gb_Ua.gb_rd{cursor:pointer}.gb_Ua.gb_rd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_rd:focus,.gb_Ua.gb_rd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_rd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_rd{background:#1a73e8;border:1px solid transparent}.gb_Fa.gb_cc .gb_rd{padding:9px 15px;min-width:80px}.gb_Sd{text-align:left}#gb .gb_Mc a.gb_rd:not(.gb_H),#gb.gb_Mc a.gb_rd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ua.gb_H.gb_rd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Mc a.gb_rd:hover:not(.gb_H),#gb.gb_Mc a.gb_rd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ua.gb_H.gb_rd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Mc a.gb_rd:focus:not(.gb_H),#gb .gb_Mc a.gb_rd:focus:hover:not(.gb_H),#gb.gb_Mc a.gb_rd:focus:not(.gb_H),#gb.gb_Mc a.gb_rd:focus:hover:not(.gb_H){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ua.gb_H.gb_rd:focus,#gb a.gb_Ua.gb_H.gb_rd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Mc a.gb_rd:active:not(.gb_H),#gb.gb_Mc a.gb_rd:active{background:#ecf3fe}#gb a.gb_Ua.gb_H.gb_rd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_K{display:none}@media screen and (max-width:319px){.gb_md .gb_J{display:none;visibility:hidden}}.gb_Wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Wa.gb_H{background-color:transparent;border:1px solid #5f6368}.gb_3a{display:inherit}.gb_Wa.gb_H .gb_3a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Wa.gb_H:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Wa:focus-visible,.gb_Wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Wa.gb_H:focus-visible,.gb_Wa.gb_H:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Wa.gb_H:active,.gb_Wa.gb_Uc.gb_H:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_4a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Wa.gb_H .gb_4a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_4a.gb_5a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_4a.gb_5a .gb_Jc{vertical-align:middle}.gb_Fa:not(.gb_cc) .gb_Wa{margin-left:10px;margin-right:4px}.gb_Td{max-height:32px;width:78px}.gb_Wa.gb_H .gb_Td{max-height:26px;width:72px}.gb_P{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_eb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_eb.gb_P{height:30px;width:30px}.gb_eb.gb_P:hover,.gb_eb.gb_P:active{-webkit-box-shadow:none;box-shadow:none}.gb_fb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_wc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_P::before,.gb_gb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_3 .gb_gb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_P:hover,.gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_P:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_P:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_hb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_hb{width:auto}.gb_hb:hover,.gb_hb:focus{opacity:.85}.gb_hd .gb_hb,.gb_hd .gb_Wd{line-height:26px}#gb#gb.gb_hd a.gb_hb,.gb_hd .gb_Wd{font-size:11px;height:auto}.gb_ib{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Za:hover .gb_ib{opacity:.85}.gb_Wa>.gb_z{padding:3px 3px 3px 4px}.gb_Xd.gb_od{color:#fff}.gb_1 .gb_hb,.gb_1 .gb_ib{opacity:1}#gb#gb.gb_1.gb_1 a.gb_hb,#gb#gb .gb_1.gb_1 a.gb_hb{color:#fff}.gb_1.gb_1 .gb_ib{border-top-color:#fff;opacity:1}.gb_ka .gb_P:hover,.gb_1 .gb_P:hover,.gb_ka .gb_P:focus,.gb_1 .gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Zd .gb_z,.gb_0d .gb_z{position:absolute;right:1px}.gb_z.gb_0,.gb_jb.gb_0,.gb_Za.gb_0{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_1d.gb_2d .gb_hb{width:30px!important}.gb_3d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_4d .gb_3d,.gb_5d .gb_3d{right:0;top:0}.gb_z .gb_B{padding:4px}.gb_S{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.G3ryJmW2kfo.2019.O","co.in","en","425",0,[4,2,"","","","787805422","0"],null,"Q_eKaLXXCu6pwN4P6-7goAE",null,0,"og.qtm.WTFD-Esq6Ic.L.W.O","AA2YrTswlII6y8v-5K9q9_iIzkDRmIbi1w","AA2YrTucqiq4kwAJLLHNcPdfuf5eZ8r2Fg","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","vishalramteke402@gmail.com","","AIhRldJVQDttTbAvUkpPmmRCUoOC1GqocRFtUYf_TEwwQVp44Nv0FuBb-pGEMFxFT58inwliGjrC0iJYpuA2RK0dFYCm9u8A8A",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",0,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.EYOBbsN3I2A.O/d=1/rs=AHpOoo_iiC5gORPbsAUenRY5t2mRSbS18A/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20250602.0_p0","en",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en","787805422.0",8,null,1,0,null,null,null,null,"3700949",null,null,null,"Q_eKaLXXCu6pwN4P6-7goAE",0,0,0,null,2,5,"nn",53,0,0,null,null,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.G3ryJmW2kfo.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTswlII6y8v-5K9q9_iIzkDRmIbi1w"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.WTFD-Esq6Ic.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTucqiq4kwAJLLHNcPdfuf5eZ8r2Fg"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",null,1,0],0,1,null,1,1,null,null,null,null,0,0,0,null,0,0,null,null,null,null,null,null,null,null,null,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/\u0026timeStmp=1753937731\u0026secTok=.AG5fkS_B4y-Y0Atmn5WOCjUprsmlaSuhiw\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",null,null,0,null,null,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,null,null,0,null,0,0,"8559284470",0,0,0],0,null,null,null,1,0,"vishalramteke402@gmail.com",0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles_gbar_=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Fa,Ga,$a,cb,eb,jb,fb,lb,rb,Db,Eb,Fb,Gb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.yk=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Ea=function(a,b){return b===void 0?a.j!==Da&&!!(2&(a.fa[_.v]|0)):!!(2&b)&&a.j!==Da};Fa=function(a){return a};Ga=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ha=function(a){a=Error(a);Ga(a,"warning");return a};_.Ja=function(a,b){if(a!=null){var c;var d=(c=Ia)!=null?c:Ia={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ga(a,"incident"),_.ka(a))}};
_.La=function(a){if(typeof a!=="boolean")throw Error("s`"+_.Ka(a)+"`"+a);return a};_.Ma=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Oa=function(a){if(!(0,_.Na)(a))throw _.Ha("enum");return a|0};_.Pa=function(a){return a==null?a:(0,_.Na)(a)?a|0:void 0};_.Qa=function(a){if(typeof a!=="number")throw _.Ha("int32");if(!(0,_.Na)(a))throw _.Ha("int32");return a|0};_.Ra=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};
_.Sa=function(a){return a==null||typeof a==="string"?a:void 0};_.Va=function(a,b,c){if(a!=null&&a[_.Ta]===_.Ua)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Ya=function(a){const b=_.Wa(_.Xa);return b?a[b]:void 0};$a=function(a,b){b<100||_.Ja(Za,1)};
cb=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Wa(_.Xa),g;!e&&f&&(g=a[f])&&g.vd($a);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=ab)!=null?r:Fa)(g-p,p,a,k,void 0)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const D=r-p;var q=void 0;((q=b)!=null?q:b={})[D]=w}else f[r]=w}if(k)for(let w in k){q=
k[w];if(q==null||(q=c(q,d))==null)continue;h=+w;let D;if(m&&!Number.isNaN(h)&&(D=h+p)<g)f[D]=q;else{let Q;((Q=b)!=null?Q:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Wa(_.Xa)&&(a=_.Ya(a))&&"function"==typeof _.bb&&a instanceof _.bb&&(f[_.Xa]=a.i());return f};
eb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.db)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:cb(a,b,eb)}if(a!=null&&a[_.Ta]===_.Ua)return fb(a);if("function"==typeof _.gb&&a instanceof _.gb)return a.j();return}return a};jb=function(a,b){if(b){ab=b==null||b===Fa||b[hb]!==ib?Fa:b;try{return fb(a)}finally{ab=void 0}}return fb(a)};
fb=function(a){a=a.fa;return cb(a,a[_.v]|0,eb)};
_.mb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-8380417|(b&1023)<<13)}else{if(!Array.isArray(a))throw Error("t");e=a[_.v]|0;if(kb&&1&e)throw Error("u");2048&e&&!(2&e)&&lb();if(e&256)throw Error("v");if(e&64)return d!==0||e&2048||(a[_.v]=e|2048),a;if(c&&(e|=128,c!==a[0]))throw Error("w");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("y");for(var h in k)if(f=+h,f<
g)c[f+b]=k[h],delete k[h];else break;e=e&-8380417|(g&1023)<<13;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("z");e=e&-8380417|(h&1023)<<13}}}e|=64;d===0&&(e|=2048);a[_.v]=e;return a};lb=function(){if(kb)throw Error("x");_.Ja(nb,5)};
rb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.ob(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Ta]===_.Ua)return b=a.fa,c=b[_.v]|0,_.Ea(a,c)?a:_.pb(a,b,c)?_.qb(a,b):_.ob(b,c);if("function"==typeof _.gb&&a instanceof _.gb)return a};_.qb=function(a,b,c){a=new a.constructor(b);c&&(a.j=Da);a.o=Da;return a};
_.ob=function(a,b,c,d){d!=null||(d=!!(34&b));a=cb(a,b,rb,d);d=32;c&&(d|=2);b=b&8380609|d;a[_.v]=b;return a};_.tb=function(a){const b=a.fa,c=b[_.v]|0;return _.Ea(a,c)?_.pb(a,b,c)?_.qb(a,b,!0):new a.constructor(_.ob(b,c,!1)):a};_.ub=function(a){if(a.j!==Da)return!1;var b=a.fa;b=_.ob(b,b[_.v]|0);b[_.v]|=2048;a.fa=b;a.j=void 0;a.o=void 0;return!0};_.vb=function(a){if(!_.ub(a)&&_.Ea(a,a.fa[_.v]|0))throw Error();};_.wb=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.pb=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.j=Da,!0):!1};_.xb=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>13&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};
_.zb=function(a,b,c,d,e){let f=!1;d=_.yb(a,d,e,g=>{const h=_.Va(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Ea(d)&&_.wb(a,b),d};_.Ab=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Bb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Cb=function(a){for(const b in a)return!1;return!0};Db=Object.defineProperty;
Eb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Fb=Eb(this);Gb=function(a,b){if(b)a:{var c=Fb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Db(c,a,{configurable:!0,writable:!0,value:b})}};Gb("globalThis",function(a){return a||Fb});
Gb("Symbol.dispose",function(a){return a?a:Symbol("b")});Gb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});
Gb("Array.prototype.flat",function(a){return a?a:function(b){b=b===void 0?1:b;var c=[];Array.prototype.forEach.call(this,function(d){Array.isArray(d)&&b>0?(d=Array.prototype.flat.call(d,b-1),c.push.apply(c,d)):c.push(d)});return c}});var Jb,Kb,Nb;_.Hb=_.Hb||{};_.t=this||self;Jb=function(a){var b=_.Ib("WIZ_global_data.oxN3nb");a=b&&b[a];return a!=null?a:!1};Kb=_.t._F_toggles_gbar_||[];_.Ib=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ka=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Lb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Mb="closure_uid_"+(Math.random()*1E9>>>0);
Nb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Nb;return _.z.apply(null,arguments)};_.Ob=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Wa=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.mk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Pb=!!(Kb[0]>>15&1),Qb=!!(Kb[0]>>16&1),Rb=!!(Kb[0]&128);var na=Pb?Qb:Jb(610401301),kb=Pb?Rb:Jb(748402147);_.Sb=_.ba(a=>a!==null&&a!==void 0);var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Vb,Tb,Wb,Ub;_.db=_.ba(a=>fa?a>=Tb&&a<=Ub:a[0]==="-"?ja(a,Vb):ja(a,Wb));Vb=Number.MIN_SAFE_INTEGER.toString();Tb=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;Wb=Number.MAX_SAFE_INTEGER.toString();Ub=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Xb=typeof TextDecoder!=="undefined";_.Yb=typeof TextEncoder!=="undefined";var oa,Zb=_.t.navigator;oa=Zb?Zb.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.$b=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.ac=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.bc=function(a){_.bc[" "](a);return a};_.bc[" "]=function(){};var pc;_.cc=_.ra();_.dc=_.sa();_.ec=_.u("Edge");_.fc=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.hc=_.ma()&&!_.u("Edge");_.ic=_.za();_.jc=wa()?oa.platform==="Windows":_.u("Windows");_.kc=wa()?oa.platform==="Android":_.u("Android");_.lc=xa();_.mc=_.u("iPad");_.nc=_.u("iPod");_.oc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.fc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.ec)return/Edge\/([\d\.]+)/.exec(c);if(_.dc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.hc)return/WebKit\/(\S+)/.exec(c);if(_.cc)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.dc){var qc;const c=_.t.document;qc=c?c.documentMode:void 0;if(qc!=null&&qc>parseFloat(a)){pc=String(qc);break a}}pc=a}_.rc=pc;_.sc=_.ta();_.tc=xa()||_.u("iPod");_.uc=_.u("iPad");_.vc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.wc=ua();_.xc=_.va()&&!_.ya();var Za,nb,hb;_.Xa=_.Ca();_.yc=_.Ca();Za=_.Ca();_.zc=_.Ca();nb=_.Ca();_.Ta=_.Ca("m_m",!0);hb=_.Ca();_.Ac=_.Ca();var Cc;_.v=_.Ca("jas",!0);Cc=[];Cc[_.v]=7;_.Bc=Object.freeze(Cc);var Da;_.Ua={};Da={};_.Dc=Object.freeze({});var ib={};var Ia=void 0;_.Ec=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Fc=Number.isSafeInteger;_.Na=Number.isFinite;_.Gc=Math.trunc;var ab;_.Hc=_.ia(0);_.Ic={};_.Jc=function(a,b,c,d,e){b=_.yb(a.fa,b,c,e);if(b!==null||d&&a.o!==Da)return b};_.yb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Kc=function(a,b,c,d){_.vb(a);const e=a.fa;_.xb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.fa,f=e[_.v]|0;b=_.zb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Ea(a,f)){const g=_.tb(b);g!==b&&(_.ub(a)&&(e=a.fa,f=e[_.v]|0),b=g,f=_.xb(e,f,c,b,d),_.wb(e,f))}return b};_.E=function(a,b,c){c==null&&(c=void 0);_.Kc(a,b,c);c&&!_.Ea(c)&&_.wb(a.fa);return a};_.Lc=function(a,b,c,d){return _.Pa(_.Jc(a,b,c,d))};_.F=function(a,b,c=!1,d){let e;return(e=_.Ma(_.Jc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Sa(_.Jc(a,b,d)))!=null?e:c};
_.I=function(a,b,c){return _.Sa(_.Jc(a,b,c,_.Ic))};_.J=function(a,b,c,d){return _.Kc(a,b,c==null?c:_.La(c),d)};_.K=function(a,b,c){return _.Kc(a,b,c==null?c:_.Qa(c))};_.L=function(a,b,c,d){return _.Kc(a,b,_.Ra(c),d)};_.N=function(a,b,c,d){return _.Kc(a,b,c==null?c:_.Oa(c),d)};_.O=class{constructor(a,b,c){this.fa=_.mb(a,b,c)}toJSON(){return jb(this)}wa(a){return JSON.stringify(jb(this,a))}};_.O.prototype[_.Ta]=_.Ua;_.O.prototype.toString=function(){return this.fa.toString()};_.Mc=_.Ab();_.Nc=_.Ab();_.Oc=_.Ab();_.Pc=Symbol();var Qc=class extends _.O{constructor(a){super(a)}};_.Sc=class extends _.O{constructor(a){super(a)}D(a){return _.K(this,3,a)}};var Tc=class extends _.O{constructor(a){super(a)}Wb(a){return _.L(this,24,a)}};_.Uc=class extends _.O{constructor(a){super(a)}};_.P=function(){this.qa=this.qa;this.Y=this.Y};_.P.prototype.qa=!1;_.P.prototype.isDisposed=function(){return this.qa};_.P.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.P.prototype[Symbol.dispose]=function(){this.dispose()};_.P.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Vc=class extends _.P{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}tb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].tb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Xc=class extends _.P{constructor(){var a=_.Wc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Yc=class extends _.O{constructor(a){super(a)}};var Zc=class extends _.O{constructor(a){super(a)}};var bd;_.$c=function(a,b,c=98,d=new _.Sc){if(a.i){const e=new Qc;_.L(e,1,b.message);_.L(e,2,b.stack);_.K(e,3,b.lineNumber);_.N(e,5,1);_.E(d,40,e);a.i.log(c,d)}};bd=class{constructor(){var a=ad;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Sc){_.$c(this,a,98,c)}};var cd,dd;cd=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.$b(c,b,a)}catch(d){console.error(d)}}}};_.ed=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new dd(a,b,c));cd(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("D");this.i=a;cd(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("D");this.j=a;cd(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
dd=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.fd=a=>{var b="qc";if(a.qc&&a.hasOwnProperty(b))return a.qc;b=new a;return a.qc=b};_.R=class{constructor(){this.v=new _.ed;this.i=new _.ed;this.D=new _.ed;this.B=new _.ed;this.C=new _.ed;this.A=new _.ed;this.o=new _.ed;this.j=new _.ed;this.F=new _.ed;this.G=new _.ed}K(){return this.v}qa(){return this.i}O(){return this.D}M(){return this.B}P(){return this.C}L(){return this.A}Y(){return this.o}J(){return this.j}N(){return this.F}static i(){return _.fd(_.R)}};var jd;_.hd=function(){return _.C(_.gd,Tc,1)};_.id=function(){return _.C(_.gd,_.Uc,5)};jd=class extends _.O{constructor(a){super(a)}};var kd;window.gbar_&&window.gbar_.CONFIG?kd=window.gbar_.CONFIG[0]||{}:kd=[];_.gd=new jd(kd);var ad=_.C(_.gd,Zc,3)||new Zc;_.hd()||new Tc;_.Wc=new bd;_.A("gbar_._DumpException",function(a){_.Wc?_.Wc.log(a):console.error(a)});_.ld=new Xc;var nd;_.od=function(a,b){var c=_.md.i();if(a in c.i){if(c.i[a]!=b)throw new nd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Cb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.md=class{constructor(){this.i={};this.j={}}static i(){return _.fd(_.md)}};_.pd=class extends _.aa{constructor(){super()}};nd=class extends _.pd{};_.A("gbar.A",_.ed);_.ed.prototype.aa=_.ed.prototype.then;_.A("gbar.B",_.R);_.R.prototype.ba=_.R.prototype.qa;_.R.prototype.bb=_.R.prototype.O;_.R.prototype.bd=_.R.prototype.P;_.R.prototype.bf=_.R.prototype.K;_.R.prototype.bg=_.R.prototype.M;_.R.prototype.bh=_.R.prototype.L;_.R.prototype.bj=_.R.prototype.Y;_.R.prototype.bk=_.R.prototype.J;_.R.prototype.bl=_.R.prototype.N;_.A("gbar.a",_.R.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var qd=new Vc;_.od("api",qd);
var rd=_.id()||new _.Uc,sd=window,td=_.y(_.I(rd,8));sd.__PVT=td;_.od("eq",_.ld);
}catch(e){_._DumpException(e)}
try{
_.ud=class extends _.O{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var vd=class extends _.O{constructor(a){super(a)}};var wd=class extends _.P{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.I(a,1));_.Ma(_.Jc(a,12))!=null&&(d.dpo=_.x(_.F(a,12)));d.ms=_.y(_.I(a,2));d.m=_.y(_.I(a,3));d.l=[];_.G(b,1)&&(a=_.I(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.I(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var xd=_.C(_.gd,_.Yc,14);if(xd){var yd=_.C(_.gd,_.ud,9)||new _.ud,zd=new vd,Bd=new wd;Bd.init(xd,yd,zd);_.od("gs",Bd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_vishalramteke402@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./bankapp_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250729-060053_RC00_788359736'; var colabScsVersion = '94dbbfc74e8ad0671885a4ed6cd31364'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_nvidia_cudf_facts_to_chat_context\x22: true, \x22add_prompt_cell\x22: false, \x22agent_client_update_task_max_request_size_bytes\x22: 10000000, \x22agent_scroll_delay_ms\x22: 200, \x22agent_update_task_max_request_size_bytes\x22: 10000000, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_service_endpoint\x22: \x22https:\/\/colab.pa.googleapis.com\x22, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_readonly_cells\x22: true, \x22allow_subpaths_in_kernel_url\x22: false, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22bigquery_sql_engine\x22: false, \x22bigquery_sql_engine_library\x22: \x22\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22cell_ui_refresh\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22cloud_run\x22: false, \x22code_report_millis\x22: 600000, \x22colab_fetch_try_reauth\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: true, \x22composer_bigquery_context\x22: false, \x22composer_context_max_variable_length\x22: 500000, \x22composer_focused_cell_context\x22: true, \x22composer_fp_context\x22: false, \x22composer_generate_code\x22: true, \x22composer_kernel_files_in_context\x22: false, \x22composer_model_strategy\x22: 0, \x22composer_show_debug_info\x22: false, \x22composer_survey\x22: true, \x22composer_transform_code\x22: true, \x22composer_visible_cells_context\x22: false, \x22converse_notebook_context_length\x22: 40000, \x22copy_cell_output\x22: false, \x22corp_third_party_widgets\x22: false, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22data_inspector\x22: false, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecate_unpin\x22: false, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22dsa_markdown_cells\x22: false, \x22dsa_sample_datasets_toast\x22: true, \x22embedded_toolbar_customization\x22: true, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_composer_code_report\x22: false, \x22enable_composer_suggestion_chips\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_edu_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_status_propagation\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22import_data\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22is_prober\x22: false, \x22jspb_analytics\x22: true, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_backend_runtime_selector\x22: false, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: false, \x22kaggle_submit_to_competition\x22: false, \x22kernel_use_connected_endpoint_for_unassign\x22: true, \x22kernel_utils_fetch\x22: false, \x22key_promoter\x22: false, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22moma_rag_composer\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: false, \x22multi_modal_context_for_transform\x22: false, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prepare_runtime_for_notebook\x22: false, \x22prereq_cells_next_steps\x22: true, \x22presentation_mode\x22: true, \x22presentation_mode_start_from_beginning\x22: false, \x22prevent_ai_long_response_generate\x22: false, \x22prevent_ai_long_response_generate_with_df\x22: false, \x22prevent_ai_long_response_suggest_fix\x22: false, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22refocus_focused_code_cell\x22: true, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22remove_ai_generate_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22runtime_version_names\x22: \x5b\x222025.07\x22\x5d, \x22runtime_version_selector\x22: false, \x22runtime_version_tags\x22: \x5b\x22release-colab_20250715-060042_RC00\x22\x5d, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: true, \x22show_empty_notebook_actions\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22signup_ccu_increase\x22: true, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_chars_limit\x22: -1, \x22smartpaste_serving_config\x22: \x22freeform_servomatic_goose_v3_xs_smart_paste\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22sql_completion_lsp\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22suggest_plots\x22: true, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 4000, \x22task_service_poll_interval_growth_factor\x22: 1.3, \x22task_service_poll_interval_ms\x22: 500, \x22task_service_poll_timeout_ms\x22: 90000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22term4all\x22: true, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22trim_filename_extension\x22: false, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_ai_service\x22: false, \x22use_colab_adk_service\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22, \x22V28\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22want_completions_ai_consent_campaign\x22: true, \x22workstations\x22: false, \x22ids\x22: \x5b20730369, 20730177, 20730183, 20730410, 20730439, 20730454, 20730150, 20730324, 20730426, 20730469, 20730265, 20730393, 20730375, 20730363\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_nvidia_cudf_facts_to_chat_context\x22: 45685179, \x22add_prompt_cell\x22: 45644995, \x22agent_client_update_task_max_request_size_bytes\x22: 45712580, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_service_endpoint\x22: 45714379, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_readonly_cells\x22: 45671718, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22bigquery_sql_engine\x22: 45697421, \x22bigquery_sql_engine_library\x22: 45700104, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22cell_ui_refresh\x22: 45673630, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22cloud_run\x22: 45697172, \x22code_report_millis\x22: 45658073, \x22colab_fetch_try_reauth\x22: 45713304, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_bigquery_context\x22: 45710683, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_focused_cell_context\x22: 45697545, \x22composer_fp_context\x22: 45701859, \x22composer_generate_code\x22: 45702500, \x22composer_kernel_files_in_context\x22: 45701855, \x22composer_model_strategy\x22: 45711731, \x22composer_show_debug_info\x22: 45700003, \x22composer_survey\x22: 45707270, \x22composer_transform_code\x22: 45700458, \x22composer_visible_cells_context\x22: 45716167, \x22converse_notebook_context_length\x22: 45705427, \x22copy_cell_output\x22: 45712093, \x22corp_third_party_widgets\x22: 45678906, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecate_unpin\x22: 45701465, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22dsa_markdown_cells\x22: 45707419, \x22dsa_sample_datasets_toast\x22: 45682045, \x22embedded_toolbar_customization\x22: 45692827, \x22embedded_use_websockets\x22: 45691694, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_composer_code_report\x22: 45708595, \x22enable_composer_suggestion_chips\x22: 45710464, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_edu_subscription_ui\x22: 45693272, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_status_propagation\x22: 45644828, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22import_data\x22: 45430411, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22is_prober\x22: 45429104, \x22jspb_analytics\x22: 45704358, \x22jsraw\x22: 45425557, \x22kaggle_backend_runtime_selector\x22: 45704319, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22kaggle_submit_to_competition\x22: 45693906, \x22kernel_use_connected_endpoint_for_unassign\x22: 45684913, \x22kernel_utils_fetch\x22: 45708200, \x22key_promoter\x22: 45425570, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22moma_rag_composer\x22: 45706746, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22multi_modal_context_for_transform\x22: 45687634, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prepare_runtime_for_notebook\x22: 45699118, \x22prereq_cells_next_steps\x22: 45640400, \x22presentation_mode\x22: 45699417, \x22presentation_mode_start_from_beginning\x22: 45714276, \x22prevent_ai_long_response_generate\x22: 45680972, \x22prevent_ai_long_response_generate_with_df\x22: 45681123, \x22prevent_ai_long_response_suggest_fix\x22: 45681124, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22refocus_focused_code_cell\x22: 45714009, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22runtime_version_names\x22: 45714997, \x22runtime_version_selector\x22: 45713197, \x22runtime_version_tags\x22: 45714998, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_empty_notebook_actions\x22: 45677304, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22signup_ccu_increase\x22: 45689970, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_chars_limit\x22: 45714219, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22sql_completion_lsp\x22: 45688254, \x22suggest_plots\x22: 45696393, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22trim_filename_extension\x22: 45691676, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_ai_service\x22: 45713338, \x22use_colab_adk_service\x22: 20730464, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'vishalramteke402@gmail.com'; var colabRenderDataToken = 'AFWLbD1uynGdZ1LQvnYRTG3cBRuB7FKa58rQ7CtidV65hME31gAp5tZTtrYGb9VMNQniUUuwCHGF2TL6Kc-DT7xbG2z8e8S7HCx0'; var colabConfig = '\x5b\x5b\x22vishalramteke402@gmail.com\x22,\x5b1,\x22AHXL0D1YQ1zs2kV+3fBZ4CSenJrP2y9BF06+++bFaLBJSIjP8QSDTHJ7kKvWQEiHihI1tZk5P3FfVVhE3KvnafkFABh9IMHPTkj8qG8yTaL96J1b5PMso5T9k5S85lCpn3g10uNL4hMx+78+8xYztNf5zl1P8lPXOn6pmRQwT8vFP36O5Ag2DDekgglK0Mcufa89UHoVwMkVO8+KOFZJIC2JmWUBNs8eUfy6i8r6\/uO+kBczJjb9vWyS9ciYQz2uDE\/AUBVPRnhhYXHVDiQjaQuh7S+LMmfmMuX0gj+5YvagQLbGvFxUs\/o7gMjLS2aRYs44J1WkQNNB69gUQL6Z6seykLBHumVU2ACO+KOzrgAHduzDbMjIwFwzYdmr3rgeG4vZp85JVHkzP0I9FXM3IRFGOJjk3ERDWKX9YgmfS4pfRCgcDcAqv5wVXRdMObhSGhfIxV6aKFFVNa42l2KkJTi2gqaRTfhwWMRfnAijYVYJMpjdYf8UpXO+3jNjknRWaOdqYnHUNTtuTXIhX+8VK6m7NtMqQR3wZyKN2qbYRqumwAq+k6HX87aPzlAXVwXFOb4wSSbBTYPEcgXcsZABDijeaKIGGriCaYBaiEcpnZzJFeKUKWMqeRKkKrDPeSIjFox1RJd\/\/UA0BtAADE8JlHjKoheNHhUFVyRTfAZdsaxtkNM84gvGVVuWshcPI9wUcU9U64dMXLKEqJ7uSpd5A8+m+8IQgYFu6NHfs6DKXO8eZPcU7Mnx7PGw44pnv9UJFJFIUPhtED5Faj+oUvT3Rt3Zk2vmbnSXlcVyQXifB9B3Da7qjou0YMMl1\/L5kBE0b9B88jvr\/BWU9aMMhysu1RknsnDJU3aTbQdTnXPyFZvshQr13RSkM3ec2ze9GmLW1dkn7dWOai6KOCfLDoyplxV17Iym+Y9iHl2OlC4MbHK2gWZ++H6F+OGwY4VzQGz9fa+Pf+oWz3YEePMC3nK6w6BVs+l090QEcGo5CqTT8V6qMR9tMkmSYgbTdnx2vPU8y1hdZPkbRa38SB40LZwTdLBfz5kyyiwE5bCzvVk1NwwlILM7dMQGpEDMSaglJ0cOybMqurs3BRl2YbJ2KqARctkBQ7ypmtGEouWXx3QXtyWytCSEKLORjCiZzsWOs2LvOi70J+1fUy4k1E0EKPvZEOBefNw0IVU57d3FMbhhkonBuEwhTPMzooQsxwx837V30g3YyaZc3xd+4rmLFHCN2rq7qC+idXPksk0glxxcAIxSM8tu3lh9msppbYE5M3qDw\/EiW9RHjLKPcmPwpNxTiB+PyGTvThz5io+TIUKq+Gm9En8G3O5jv12JAwSH+DSCodPVkUtSGPlUcSqab7X8aSZfTwz+J14b6My3Ct4tEoce6BzIvFpgiVrSWHlqfU\/SgSGhOJjrtrL\/DpwD4WuWrsmdN6u80fiTFZpJy33i6EuKVvRisMAMpCJaPVX8G8qogvdvKWv4PBc6fdG1uwbP7UjZNCGOS6IB7EROaSFL4qQl1ECV7tNJKuGT4KGqA\/N3ZEW+5WNjzDCho1Ys99gbEP+aI4dKlWvaQ6ZH7jtT5EMmCQONdAGoDxoJBcLo+g\/nLhBgcvfMc8DX\/AF9RSprAnvqWsgibZg3erjzO8\/CRBgjhmdDaFxnmkal\/Sxzrcv\/S2b2LgjN4QNg1m25k3SpklLWy0L1gdauBJVPugY6jWbxJ5cHHWXM1i7y7zzg1n6kAi1yFQEqWfMnHREUqfZg8cU7qAYmgwSrSxVU2cquqZc86ep1Q32acSJScQUqbuuuwIkv+PGF7DTBwR2acXO2HgL\/jH9JmeRtpugOQL\/HpgSO7D8+6a5nQHL4r+8L+BhQyEalPblPG6JZBpOK2lZMGeu82eXuVj8iGYvZaj\/Gq+e4hKaQNWTiBKU\x3d\x22,\x22AJ9oCCzSEQnFRrdjWVxIm5oRcDZ58GNLIZmMrBBeaCbvA65elUIbK4eMXjv8NWCfha2w6PBgpl1DwdcdecPBx8NTwdustmzbUOUN5qknTgGf5+G3kcfEJOyBjjOYx2h+rsT7yn2dm+GO\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22,0,0,0\x5d,\x5b1,4,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/94dbbfc74e8ad0671885a4ed6cd31364/img/favicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./bankapp_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="async" type="text/javascript" src="./bankapp_files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./bankapp_files/rs=AA2YrTswlII6y8v-5K9q9_iIzkDRmIbi1w" nonce=""></script><link type="text/css" href="./bankapp_files/rs=AA2YrTucqiq4kwAJLLHNcPdfuf5eZ8r2Fg" rel="stylesheet"><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./bankapp_files/editor.main.css"><script async="async" type="text/javascript" src="./bankapp_files/editor.main.nls.js.download"></script><script async="async" type="text/javascript" src="./bankapp_files/markdown.js.download"></script><script src="./bankapp_files/api.js.download" nonce=""></script><script src="./bankapp_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: #234521;
--vscode-diffEditor-removedTextBackground: #5b2022;
--vscode-diffEditor-insertedLineBackground: #22331f;
--vscode-diffEditor-removedLineBackground: #3c1a1a;
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #82b76c; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #69a5d7; }
.mtk11 { color: #f28b82; }
.mtk12 { color: #d7ba7d; }
.mtk13 { color: #d49d87; }
.mtk14 { color: #dcdcdc; }
.mtk15 { color: #808080; }
.mtk16 { color: #4ec9b0; }
.mtk17 { color: #dcdcaa; }
.mtk18 { color: #f44747; }
.mtk19 { color: #82c6ff; }
.mtk20 { color: #c99cc6; }
.mtk21 { color: #c586c0; }
.mtk22 { color: #a79873; }
.mtk23 { color: #dd6a6f; }
.mtk24 { color: #5bb498; }
.mtk25 { color: #909090; }
.mtk26 { color: #778899; }
.mtk27 { color: #ff00ff; }
.mtk28 { color: #b46695; }
.mtk29 { color: #ff0000; }
.mtk30 { color: #4f76ac; }
.mtk31 { color: #3dc9b0; }
.mtk32 { color: #74b0df; }
.mtk33 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script src="./bankapp_files/api(2).js.download" nonce=""></script><script src="./bankapp_files/api(3).js.download" nonce=""></script></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./bankapp_files/gapi_loader.js.download" nonce=""></script><script src="./bankapp_files/socketio_binary.js.download" nonce=""></script><script src="./bankapp_files/analytics_binary.js.download" nonce=""></script><script src="./bankapp_files/MathJax.js.download" nonce=""></script><script src="./bankapp_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./bankapp_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$317996004$-->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$317996004$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$317996004$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$317996004$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Loading...</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_S" ng-non-bindable=""><div class="gb_Bc"><div>Google Account</div><div class="gb_g">Vishal Ramteke</div><div>vishalramteke402@gmail.com</div><div class="gb_Cc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Gd;Gd=class extends _.pd{};_.Hd=function(a,b){if(b in a.i)return a.i[b];throw new Gd;};_.Id=function(a){return _.Hd(_.md.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Ld;_.Jd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Ld=function(a){return new _.Kd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Md=globalThis.trustedTypes;_.Nd=class{constructor(a){this.i=a}toString(){return this.i}};_.Od=new _.Nd("about:invalid#zClosurez");_.Kd=class{constructor(a){this.Sh=a}};_.Pd=[Ld("data"),Ld("http"),Ld("https"),Ld("mailto"),Ld("ftp"),new _.Kd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Qd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Rd=new _.Qd(_.Md?_.Md.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Vd,ge,Ud,Wd,ae;_.Sd=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Na)(a)?a|0:void 0};_.Td=function(a,b){return a.lastIndexOf(b,0)==0};Vd=function(){let a=null;if(!Ud)return a;try{const b=c=>c;a=Ud.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Xd=function(){Wd===void 0&&(Wd=Vd());return Wd};_.Zd=function(a){const b=_.Xd();a=b?b.createScriptURL(a):a;return new _.Yd(a)};
_.$d=function(a){if(a instanceof _.Yd)return a.i;throw Error("F");};_.be=function(a){if(ae.test(a))return a};_.ce=function(a){if(a instanceof _.Nd)if(a instanceof _.Nd)a=a.i;else throw Error("F");else a=_.be(a);return a};_.de=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.S=function(a,b,c){return _.Ma(_.Jc(a,b,c,_.Ic))};_.ee=function(a,b){return _.Sd(_.Jc(a,b,void 0,_.Ic))};
_.fe=function(a){var b=_.Ka(a);return b=="array"||b=="object"&&typeof a.length=="number"};Ud=_.Md;_.Yd=class{constructor(a){this.i=a}toString(){return this.i+""}};ae=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var me,qe,he;_.je=function(a){return a?new he(_.ie(a)):ge||(ge=new he)};_.ke=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.T=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a=a?(b||c).querySelector(a?"."+a:""):_.le(c,"*",a,b)[0]||null);return a||null};_.le=function(a,b,c,d){a=d||a;return(b=b&&b!="*"?String(b).toUpperCase():"")||c?a.querySelectorAll(b+(c?"."+c:"")):a.getElementsByTagName("*")};
_.ne=function(a,b){_.Bb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:me.hasOwnProperty(d)?a.setAttribute(me[d],c):_.Td(d,"aria-")||_.Td(d,"data-")?a.setAttribute(d,c):a[d]=c})};me={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.oe=function(a){return a?a.defaultView:window};_.re=function(a,b){const c=b[1],d=_.pe(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.ne(d,c));b.length>2&&qe(a,d,b);return d};qe=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.fe(f)||_.Lb(f)&&f.nodeType>0?d(f):_.$b(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Jd(f):f,d)}};
_.se=function(a){return _.pe(document,a)};_.pe=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.te=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.ue=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.ve=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ie=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};he=function(a){this.i=a||_.t.document||document};_.n=he.prototype;
_.n.H=function(a){return _.ke(this.i,a)};_.n.Pa=function(a,b,c){return _.re(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.Ie=_.te;_.n.mg=_.ue;_.n.lg=_.ve;
}catch(e){_._DumpException(e)}
try{
_.Ki=function(a){const b=_.de("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Li=function(a){if(!a)return null;a=_.I(a,4);var b;a===null||a===void 0?b=null:b=_.Zd(a);return b};_.Mi=function(a,b,c){a=a.fa;return _.zb(a,a[_.v]|0,b,c)!==void 0};_.Ni=class extends _.O{constructor(a){super(a)}};_.Oi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Qi=function(a,b,c){a<b?Pi(a+1,b):_.Wc.log(Error("da`"+a+"`"+b),{url:c})},Pi=function(a,b){if(Ri){const c=_.se("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.$d(Ri);_.Ki(c);c.onerror=_.Ob(Qi,a,b,c.src);_.Oi("HEAD")[0].appendChild(c)}},Si=class extends _.O{constructor(a){super(a)}};var Ti=_.C(_.gd,Si,17)||new Si,Ui,Ri=(Ui=_.C(Ti,_.Ni,1))?_.Li(Ui):null,Vi,Wi=(Vi=_.C(Ti,_.Ni,2))?_.Li(Vi):null,Xi=function(){Pi(1,2);if(Wi){const a=_.se("LINK");a.setAttribute("type","text/css");a.href=_.$d(Wi).toString();a.rel="stylesheet";let b=_.de("style",document);b&&a.setAttribute("nonce",b);_.Oi("HEAD")[0].appendChild(a)}};(function(){const a=_.hd();if(_.S(a,18))Xi();else{const b=_.ee(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Xi,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><iframe id="apiproxy4f6a36cd7abbee8150217ceb91e56f175ba0d7e70.2584964049" name="apiproxy4f6a36cd7abbee8150217ceb91e56f175ba0d7e70.2584964049" src="./bankapp_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-5zna6tcy4e06" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./bankapp_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./bankapp_files/saved_resource.html"></iframe></div><iframe src="./bankapp_files/bscframe.html" style="display: none;"></iframe><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./bankapp_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical colab-left-pane-open" style="position: relative;">
      <!--?lit$317996004$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><a id="link" class="button" href="https://colab.research.google.com/drive/1pxBWnZLey56FSawqJcg4Kqa3xBBmzj-N#notebook-main"><!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </a>
    </template><!--?lit$317996004$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$317996004$-->
    <!--?lit$317996004$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning" hidden=""><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$317996004$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1pxBWnZLey56FSawqJcg4Kqa3xBBmzj-N#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$317996004$--> <!--?lit$317996004$-->

    <div id="header" class="horizontal layout">
      <div id="header-background" class="basic-corgi-mode"><div class="kitty-canvas maneki-kitty kitty-mode-fast"></div><div class="kitty-canvas kinako-kitty kitty-mode-slow"></div><div class="crab-mode basic-crab"></div></div>
      <div id="header-content">
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><div id="header-logo">
              <!--?lit$317996004$--> <!--?lit$317996004$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$317996004$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$--><svg viewBox="0 0 24 24"><!--?lit$317996004$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$317996004$--> <!--?lit$317996004$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 96.7px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">bank.ipynb_</colab-input-sizer>
            <!--?lit$317996004$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$317996004$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$317996004$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$317996004$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$317996004$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$317996004$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$317996004$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$317996004$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$317996004$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$317996004$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$317996004$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$317996004$-->
      <!--?lit$317996004$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$317996004$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$317996004$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$317996004$--> <md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button" aria-label="Share notebook">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->people</md-icon>
                <!--?lit$317996004$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$317996004$--> <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button" aria-label="Toggle Gemini">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$317996004$-->Gemini
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$317996004$-->
    <!--?lit$317996004$--> <colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
        <!--?lit$317996004$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$317996004$--><span class="screenreader-only"><!--?lit$317996004$-->Show command palette <!--?lit$317996004$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$317996004$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$317996004$-->Commands
          </colab-toolbar-button>
          <span class="colab-separator"></span>
    <!--?lit$317996004$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
        <!--?lit$317996004$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$317996004$--><span class="screenreader-only"><!--?lit$317996004$-->Insert code cell below <!--?lit$317996004$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$317996004$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$317996004$-->Code
          </colab-toolbar-button>
          <!--?lit$317996004$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
        <!--?lit$317996004$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$317996004$--><span class="screenreader-only"><!--?lit$317996004$-->Add text cell <!--?lit$317996004$--></span>
      </md-text-button>
      <!--?lit$317996004$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$317996004$-->Text
          </colab-toolbar-button>
        
    <span class="colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Run all cells in notebook"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
        <!--?lit$317996004$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$317996004$--><span class="screenreader-only"><!--?lit$317996004$-->Run all cells in notebook <!--?lit$317996004$--></span>
      </md-text-button>
      <!--?lit$317996004$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Run all cells in notebook" shortcut=""><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Run all cells in notebook</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$317996004$-->Run all
      </colab-toolbar-button>
      <!--?lit$317996004$--><md-icon-button data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$317996004$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$317996004$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$317996004$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$317996004$--><!----><md-menu-item command="restart" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$317996004$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$317996004$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$317996004$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$317996004$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$317996004$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$317996004$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$317996004$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$317996004$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$317996004$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$317996004$-->Restart session and run all</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$317996004$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$317996004$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$317996004$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$317996004$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$317996004$-->Interrupt execution</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$317996004$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$317996004$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$317996004$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$317996004$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$317996004$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$317996004$-->
    <!--?lit$317996004$-->
    <!--?lit$317996004$-->
    <!--?lit$317996004$-->
    <!--?lit$317996004$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>

    <!--?lit$317996004$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$317996004$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$317996004$--><!--?lit$317996004$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$317996004$--> <!--?lit$317996004$--><md-icon-button id="connect-icon" disabled="" class="icon-warning" data-aria-label="Focus the last run cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Focus the last run cell" disabled="">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->more_horiz</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger for="connect-icon" id="connect-icon-tooltip" aria-hidden="true" message="Focus the last run cell"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Focus the last run cell</div><!----><!--?--></template>
          </colab-tooltip-trigger>
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="" disabled=""><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="true"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
        <!--?lit$317996004$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$317996004$--><span class="screenreader-only"><!--?lit$317996004$--> <!--?lit$317996004$--></span>
      </md-text-button>
      <!--?lit$317996004$--><!--?--></template>
        <!--?lit$317996004$-->Connecting
      </colab-toolbar-button>
      <!--?lit$317996004$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$317996004$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$317996004$-->
    <span class="collapsed-options">
      <!--?lit$317996004$--><span class="colab-separator"></span>
      <!--?lit$317996004$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$317996004$--> <md-icon-button class="show-chat-button" id="show-chat-button-toolbar" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button-toolbar" id="show-chat-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$317996004$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$317996004$--><colab-left-pane role="complementary" aria-label="left pane" class="colab-left-pane-open"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$317996004$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$317996004$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$317996004$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$317996004$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$317996004$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->code</md-icon>
    </md-icon-button> <!--?lit$317996004$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$317996004$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$317996004$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$317996004$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value="" selected=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button standard selected" aria-label="Files" aria-pressed="true">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="icon icon--selected"><slot name="selected"><slot></slot></slot></span>
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->folder</md-icon>
    </md-icon-button> <!--?lit$317996004$-->
      </div></div>
      </div><colab-resizer class="ew-resize">
          <div class="resizer-contents">
            <div class="colab-left-pane-header layout horizontal noshrink">
            <!----> <!--?lit$317996004$-->
      <h3 class="left-pane-content-title"><!--?lit$317996004$-->Files</h3>
      <!--?lit$317996004$--> <!--?lit$317996004$--><md-icon-button class="colab-left-pane-action colab-left-pane-move" data-aria-label="Move left pane to a tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move left pane to a tab">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>tab</md-icon>
    </md-icon-button> <!--?lit$317996004$--><md-icon-button class="colab-left-pane-action colab-left-pane-close" data-aria-label="Close left pane" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close left pane">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button><!--?--></div>
            <div class="left-pane-container"><colab-file-browser class="layout vertical"><colab-file-tree><!----> <!--?lit$317996004$-->
        <div class="file-tree-buttons">
          <label for="file-tree-upload-input">
            <md-icon-button class="colab-icon file-tree-upload-button" title="Upload to session storage" data-aria-label="Upload to session storage" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Upload to session storage">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
              <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload_file</md-icon>
            </md-icon-button>
          </label>
          <input id="file-tree-upload-input" type="file" multiple="">
          <md-icon-button class="file-tree-refresh" title="Refresh" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard ">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>refresh</md-icon>
          </md-icon-button>
          <md-icon-button toggle="" class="mount-drive-button" title="Mount Drive" data-aria-label="Mount Drive" aria-label-selected="Unmount Drive" style="display: flex;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mount Drive" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$--><svg viewBox="0 0 24 24"><!--?lit$317996004$-->
    <path d="M20,6H12L10,4H4A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H20a2,2,0,0,0,2-2V8A2,2,0,0,0,20,6ZM13.57,9.32,13,8.4l.34-.6h3.11l3.69,6.5H16.38M12.11,17l-.67,1.2h-1L9,15.42,12.72,9l2,3.46h0M19.3,18.2H12.09l.67-1.2,1.15-2h6.64l.34.6Z"></path></svg></md-icon>
            <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$--><svg viewBox="0 0 24 24"><!--?lit$317996004$-->
    <path d="M12.72,9l2,3.46h0l-.26.47,2,2h4.1l.34.6L19.45,18l1.69,1.69A2,2,0,0,0,22,18V8a2,2,0,0,0-2-2H12L10,4H5.5l6.4,6.4Zm.66-1.17h3.11l3.69,6.5H16.38l-2.81-5L13,8.4Z"></path>
    <path d="M22.19,22.19,1.81,1.81.4,3.22,2.25,5.07A2,2,0,0,0,2,6V18a2,2,0,0,0,2,2H17.17l3.61,3.61Zm-11.73-4L9,15.42l1.3-2.26,2.35,2.36.17.17L12.11,17l-.67,1.2Zm1.63,0,.67-1.2.51-.9,2.1,2.1Z"></path></svg></md-icon>
          </md-icon-button>
          <md-icon-button toggle="" id="hidden-files-toggle" data-aria-label="Show hidden files" aria-label-selected="Hide hidden files" title="Show hidden files" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Show hidden files" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>visibility_off</md-icon>
            <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>visibility</md-icon>
          </md-icon-button>
        </div>
        <div class="parent-link"><div class="file-title-row">
          <!--?lit$317996004$-->
                <div class="file-icon colab-icon" style="margin-left: 0px;"></div>
              
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->folder_open</md-icon>
          <span class="file-tree-name" title="Up one level">
            <!--?lit$317996004$-->..
          </span>
          <input class="file-tree-name-input" value="..">
          <!--?lit$317996004$--><md-icon-button class="file-item-action-button add-to-composer-button" id="add-to-composer-button-0" data-aria-label="Add to Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add to Gemini">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="add-to-composer-button-0" message="Add to Gemini"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Add to Gemini</div><!----><!--?--></template>
    </colab-tooltip-trigger>
          <md-icon-button class="file-item-action-button menu-button" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="More actions for file: .." value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions for file: .." aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div></div>
        <div class="files-root"><colab-file-view filename="content" draggable="true"><!----><!--?lit$317996004$--><!--?--><!--?lit$317996004$-->
        <div class="child-files"><colab-file-view filename="sample_data" class="collapsed" draggable="true"><!----><!--?lit$317996004$-->
        <div class="file-title-row">
          <!--?lit$317996004$--> <md-icon class="file-icon colab-icon directory-icon" style="margin-left: 0px;" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
          <md-icon class="file-icon colab-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->folder</md-icon>
          <span class="file-tree-name" title="sample_data">
            <!--?lit$317996004$-->sample_data
          </span>
          <input class="file-tree-name-input" value="sample_data">
          <!--?lit$317996004$-->
          <md-icon-button class="file-item-action-button menu-button" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="More actions for folder: sample_data" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions for folder: sample_data" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon></md-icon-button>
        </div>
      <!--?lit$317996004$-->
        <div class="child-files"></div>
        <div class="overflow-ellipsis" title="Directory is too large to display all files." style="margin-left: 0px;">
          …
        </div>
      <!--?--></colab-file-view></div>
        <div class="overflow-ellipsis" title="Directory is too large to display all files." style="margin-left: -20px;">
          …
        </div>
      <!--?--></colab-file-view></div>
        <div class="files-drag-to-upload layout horizontal">
          <md-icon class="layout noshrink" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload_file</md-icon>
          <div> <!--?lit$317996004$-->Drop files to upload them to session storage. </div>
        </div>
        <div class="files-uploading"></div>
        <div class="colab-usage-bar-container"></div></colab-file-tree></colab-file-browser></div>
          </div>
        <div class="resizer-thumb"></div></colab-resizer></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$317996004$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$317996004$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-nnyjHsGN1h31" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$317996004$--><div class="indicator"></div>
      </div>
      <!--?lit$317996004$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-nnyjHsGN1h31"><!--?lit$317996004$--><!--?lit$317996004$-->Notebook<!--?--></span>
            <!--?lit$317996004$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$317996004$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" tabindex="-1" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$317996004$-->
              <div class="notebook-content ">
                <!--?lit$317996004$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$317996004$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$317996004$-->Text
        </md-outlined-button>
        <!--?lit$317996004$-->
        <!--?lit$317996004$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code focused" id="cell-H58Mwchp1h3q" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$317996004$-->Gemini
    </div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" aria-disabled="true">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->arrow_upward</md-icon>
        <!--?lit$317996004$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Move cell up</div><!----><!----><div><!--?lit$317996004$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" aria-disabled="true">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->arrow_downward</md-icon>
        <!--?lit$317996004$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Move cell down</div><!----><!----><div><!--?lit$317996004$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$317996004$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-H58Mwchp1h3q" anchor="ai-menu-anchor-H58Mwchp1h3q" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$317996004$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$317996004$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$317996004$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$317996004$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$317996004$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$317996004$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$317996004$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$317996004$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$317996004$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$317996004$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$317996004$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$317996004$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$317996004$-->Explain code</span>
  </md-menu-item><!----><!----><md-menu-item command="transform-code" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$317996004$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$317996004$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$317996004$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$317996004$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$317996004$-->Transform code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-H58Mwchp1h3q-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-H58Mwchp1h3q" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-H58Mwchp1h3q" id="ai-menu-anchor-H58Mwchp1h3q-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->link</md-icon>
        <!--?lit$317996004$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copy link to cell"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Copy link to cell</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-add-comment-tooltip" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->comment</md-icon>
        <!--?lit$317996004$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Add a comment
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Add a comment</div><!----><!----><div><!--?lit$317996004$-->Ctrl+Alt+M</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->settings</md-icon>
        <!--?lit$317996004$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Open editor settings"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Open editor settings</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->edit</md-icon>
        <!--?lit$317996004$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$--><svg viewBox="0 0 24 24"><!--?lit$317996004$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
        <!--?lit$317996004$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mirror cell in tab"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Mirror cell in tab</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->delete</md-icon>
        <!--?lit$317996004$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Delete cell</div><!----><!----><div><!--?lit$317996004$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$317996004$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused stale hovered">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$317996004$--><span class="execution-count"><!--?lit$317996004$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$317996004$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$317996004$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$317996004$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$317996004$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$317996004$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="1" data-mode-id="notebook-python" style="height: 1264px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/22" style="width: 1109px; height: 1264px;"><div data-mprt="3" class="overflow-guard" style="width: 1109px; height: 1264px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 1264px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 1264px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 1264px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div><div style="position:absolute;top:1083px;width:100%;height:19px;"></div><div style="position:absolute;top:1102px;width:100%;height:19px;"></div><div style="position:absolute;top:1121px;width:100%;height:19px;"></div><div style="position:absolute;top:1140px;width:100%;height:19px;"></div><div style="position:absolute;top:1159px;width:100%;height:19px;"></div><div style="position:absolute;top:1178px;width:100%;height:19px;"></div><div style="position:absolute;top:1197px;width:100%;height:19px;"></div><div style="position:absolute;top:1216px;width:100%;height:19px;"></div><div style="position:absolute;top:1235px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1103px; height: 1264px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 1264px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1103px;"><div style="position:absolute;top:0px;width:100%;height:19px;"></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div><div style="position:absolute;top:969px;width:100%;height:19px;"></div><div style="position:absolute;top:988px;width:100%;height:19px;"></div><div style="position:absolute;top:1007px;width:100%;height:19px;"></div><div style="position:absolute;top:1026px;width:100%;height:19px;"></div><div style="position:absolute;top:1045px;width:100%;height:19px;"></div><div style="position:absolute;top:1064px;width:100%;height:19px;"></div><div style="position:absolute;top:1083px;width:100%;height:19px;"></div><div style="position:absolute;top:1102px;width:100%;height:19px;"></div><div style="position:absolute;top:1121px;width:100%;height:19px;"></div><div style="position:absolute;top:1140px;width:100%;height:19px;"></div><div style="position:absolute;top:1159px;width:100%;height:19px;"></div><div style="position:absolute;top:1178px;width:100%;height:19px;"></div><div style="position:absolute;top:1197px;width:100%;height:19px;"></div><div style="position:absolute;top:1216px;width:100%;height:19px;"></div><div style="position:absolute;top:1235px;width:100%;height:19px;"><div class="current-line" style="width:1103px; height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 1264px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1103px; height: 1264px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk10">class</span><span class="mtk1">&nbsp;BankAccount</span><span class="mtk14">:</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk10">def</span><span class="mtk1">&nbsp;</span><span class="mtk17">__init__</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk4">self</span><span class="mtk1">,&nbsp;</span><span class="mtk4">account_number</span><span class="mtk1">,&nbsp;</span><span class="mtk4">pin</span><span class="mtk1">,&nbsp;</span><span class="mtk4">balance</span><span class="mtk1">=</span><span class="mtk6">0</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.account_number&nbsp;=&nbsp;account_number</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.pin&nbsp;=&nbsp;pin</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.balance&nbsp;=&nbsp;balance</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk10">def</span><span class="mtk1">&nbsp;</span><span class="mtk17">check_pin</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk4">self</span><span class="mtk1">,&nbsp;</span><span class="mtk4">entered_pin</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">return</span><span class="mtk1">&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.pin&nbsp;==&nbsp;entered_pin</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk10">def</span><span class="mtk1">&nbsp;</span><span class="mtk17">check_balance</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk4">self</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk10">f</span><span class="mtk5">"Your&nbsp;current&nbsp;balance&nbsp;is&nbsp;₹</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk4">self</span><span class="mtk1">.balance</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk10">def</span><span class="mtk1">&nbsp;</span><span class="mtk17">deposit</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk4">self</span><span class="mtk1">,&nbsp;</span><span class="mtk4">amount</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;amount&nbsp;&gt;&nbsp;</span><span class="mtk6">0</span><span class="mtk14">:</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.balance&nbsp;+=&nbsp;amount</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk10">f</span><span class="mtk5">"₹</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk1">amount</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">&nbsp;deposited&nbsp;successfully."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">else</span><span class="mtk14">:</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Enter&nbsp;a&nbsp;valid&nbsp;amount."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk10">def</span><span class="mtk1">&nbsp;</span><span class="mtk17">withdraw</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk4">self</span><span class="mtk1">,&nbsp;</span><span class="mtk4">amount</span><span class="mtk1 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;amount&nbsp;&gt;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.balance</span><span class="mtk14">:</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Insufficient&nbsp;balance."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">elif</span><span class="mtk1">&nbsp;amount&nbsp;&lt;=&nbsp;</span><span class="mtk6">0</span><span class="mtk14">:</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Enter&nbsp;a&nbsp;valid&nbsp;amount."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">else</span><span class="mtk14">:</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk4">self</span><span class="mtk1">.balance&nbsp;-=&nbsp;amount</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk10">f</span><span class="mtk5">"₹</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk1">amount</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">&nbsp;withdrawn&nbsp;successfully."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;---&nbsp;Main&nbsp;Program&nbsp;Starts&nbsp;Here&nbsp;---</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Creating&nbsp;an&nbsp;account&nbsp;with&nbsp;dummy&nbsp;data</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk1">user_account&nbsp;=&nbsp;BankAccount</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"1234567890"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"1234"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">5000</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Asking&nbsp;for&nbsp;credentials</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span class="mtk1">entered_acc&nbsp;=&nbsp;</span><span class="mtk17">input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Enter&nbsp;your&nbsp;account&nbsp;number:&nbsp;"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk1">entered_pin&nbsp;=&nbsp;</span><span class="mtk17">input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Enter&nbsp;your&nbsp;4-digit&nbsp;PIN:&nbsp;"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Authenticate&nbsp;user</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk20">if</span><span class="mtk1">&nbsp;entered_acc&nbsp;==&nbsp;user_account.account_number&nbsp;</span><span class="mtk19">and</span><span class="mtk1">&nbsp;user_account.check_pin</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">entered_pin</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"\nLogin&nbsp;successful!\n"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">while</span><span class="mtk1">&nbsp;</span><span class="mtk9">True</span><span class="mtk14">:</span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"\nSelect&nbsp;an&nbsp;option:"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"1.&nbsp;Check&nbsp;Balance"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"2.&nbsp;Deposit"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"3.&nbsp;Withdraw"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"4.&nbsp;Exit"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:874px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:893px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;choice&nbsp;=&nbsp;</span><span class="mtk17">input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Enter&nbsp;your&nbsp;choice&nbsp;(1-4):&nbsp;"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:912px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:931px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;choice&nbsp;==&nbsp;</span><span class="mtk5">"1"</span><span class="mtk14">:</span></span></div><div style="top:950px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_account.check_balance</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:969px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">elif</span><span class="mtk1">&nbsp;choice&nbsp;==&nbsp;</span><span class="mtk5">"2"</span><span class="mtk14">:</span></span></div><div style="top:988px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;amt&nbsp;=&nbsp;</span><span class="mtk16">float</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk17">input</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk5">"Enter&nbsp;amount&nbsp;to&nbsp;deposit:&nbsp;₹"</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1007px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_account.deposit</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">amt</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1026px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">elif</span><span class="mtk1">&nbsp;choice&nbsp;==&nbsp;</span><span class="mtk5">"3"</span><span class="mtk14">:</span></span></div><div style="top:1045px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;amt&nbsp;=&nbsp;</span><span class="mtk16">float</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk17">input</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk5">"Enter&nbsp;amount&nbsp;to&nbsp;withdraw:&nbsp;₹"</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1064px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_account.withdraw</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">amt</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1083px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">elif</span><span class="mtk1">&nbsp;choice&nbsp;==&nbsp;</span><span class="mtk5">"4"</span><span class="mtk14">:</span></span></div><div style="top:1102px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Thank&nbsp;you&nbsp;for&nbsp;banking&nbsp;with&nbsp;us!"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1121px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">break</span></span></div><div style="top:1140px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">else</span><span class="mtk14">:</span></span></div><div style="top:1159px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Invalid&nbsp;choice.&nbsp;Please&nbsp;try&nbsp;again."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1178px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:1197px;height:19px;" class="view-line"><span><span class="mtk20">else</span><span class="mtk14">:</span></span></div><div style="top:1216px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Invalid&nbsp;account&nbsp;number&nbsp;or&nbsp;PIN."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1235px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 1235px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.6px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1089px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1089px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="17" height="1580" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 1264px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 1264px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 1264px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1109px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 1235px; left: 6px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1109px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 1264px;"><div class="minimap-shadow-hidden" style="height: 1264px;"></div><canvas width="0" height="1580" style="position: absolute; left: 0px; width: 0px; height: 1264px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="1580" style="position: absolute; left: 0px; width: 0px; height: 1264px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1536px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 731.94px; max-height: 316px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> <div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$317996004$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$317996004$-->Text
        </md-outlined-button>
        <!--?lit$317996004$-->
        <!--?lit$317996004$-->
      </div><hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$317996004$--> <div class="footer-links" style="padding-bottom: 65.5938px;">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$317996004$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$317996004$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -2px inset;"></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$317996004$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$317996004$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$317996004$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$317996004$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$317996004$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$317996004$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$317996004$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./bankapp_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./bankapp_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer view-mode="floating"><template shadowrootmode="open"><!---->
      <colab-composer-conversation><template shadowrootmode="open"><!---->
      <div class="scrollable">
        <!--?lit$317996004$-->
        <!--?lit$317996004$-->
      </div>
    </template>
      </colab-composer-conversation>
      <div class="footer">
        <!--?lit$317996004$-->
        <colab-composer-input><template shadowrootmode="open"><!----><div class="wrapper">
        <!--?lit$317996004$-->
        <div class="text-field-and-spark">
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          <div class="text-field-wrapper" data-value="">
            <md-outlined-text-field type="textarea" rows="1" maxlength="2000" placeholder="What can I help you build?" inputmode="" autocomplete=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <span class="text-field  textarea ">
        <!--?lit$317996004$--><md-outlined-field class="field" count="0" error-text="" label="" max="2000" resizable="" supporting-text=""><template shadowrootmode="open"><!---->
      <div class="field  resizable no-label ">
        <div class="container-overflow">
          <!--?lit$317996004$-->
          <slot name="container"></slot>
          <!--?lit$317996004$--> <!--?lit$317996004$--> <!--?lit$317996004$-->
      <div class="outline">
        <div class="outline-start"></div>
        <div class="outline-notch">
          <div class="outline-panel-inactive"></div>
          <div class="outline-panel-active"></div>
          <div class="outline-label"><!--?lit$317996004$--></div>
        </div>
        <div class="outline-end"></div>
      </div>
    
          <div class="container">
            <div class="start">
              <slot name="start"></slot>
            </div>
            <div class="middle">
              <div class="label-wrapper">
                <!--?lit$317996004$--> <!--?lit$317996004$-->
              </div>
              <div class="content">
                <slot></slot>
              </div>
            </div>
            <div class="end">
              <slot name="end"></slot>
            </div>
          </div>
        </div>
        <!--?lit$317996004$-->
      <div class="supporting-text"><!--?lit$317996004$--><span><!--?lit$317996004$--></span><!--?lit$317996004$--><span class="counter"><!--?lit$317996004$-->0 / 2000</span></div>
      <slot name="aria-describedby"></slot>
    
      </div>
    </template>
      <!--?lit$317996004$-->
      <span class="icon leading" slot="start">
        <slot name="leading-icon"></slot>
      </span>
    
      <!--?lit$317996004$-->
        <textarea class="input" aria-describedby="description" aria-invalid="false" maxlength="2000" placeholder="What can I help you build?" rows="1" cols="20"></textarea>
      
      <!--?lit$317996004$-->
      <span class="icon trailing" slot="end">
        <slot name="trailing-icon"></slot>
      </span>
    
      <div id="description" slot="aria-describedby" hidden=""><!----><!--?lit$317996004$--> <!--?lit$317996004$-->0 / 2000<!--?--></div>
      <slot name="container" slot="container"></slot>
    </md-outlined-field>
      </span>
    </template>
            </md-outlined-text-field>
          </div>
        </div>
        <div class="actions">
          <!--?lit$317996004$--><md-icon-button id="add-file" data-aria-label="Add files" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add files">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add_circle</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="add-file" message="Add files"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Add files</div><!----><!--?--></template>
      </colab-tooltip-trigger>
          <!--?lit$317996004$--><md-icon-button id="send" data-aria-label="Send" aria-describedby="send-tooltip" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Send" aria-disabled="true">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>send</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="send" id="send-tooltip" message="Send"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Send</div><!----><!--?--></template>
      </colab-tooltip-trigger>
        </div>
      </div>
      <!--?lit$317996004$--><!--?--></template></colab-composer-input>
        <!--?lit$317996004$--> <!--?lit$317996004$-->
      </div>
      <!--?lit$317996004$--><div class="floating-actions">
      <!--?lit$317996004$--><!--?lit$317996004$-->
      <md-icon-button id="move-to-side-panel" data-aria-label="Move to panel" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move to panel">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>dock_to_left</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="move-to-side-panel" message="Move to panel"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Move to panel</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    <!--?lit$317996004$--><md-icon-button id="close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="close" message="Close"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Close</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?-->
    </div>
    </template></colab-composer><colab-status-bar role="region" aria-label="Runtime status bar"><template shadowrootmode="open"><!----><span class="left">
        <slot name="bottom-pane-buttons"></slot>
      </span>
      <span class="middle"><!--?lit$317996004$-->
      <md-icon-button toggle="" id="toggle-composer" data-aria-label="Toggle Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini" aria-pressed="false">
        <!--?lit$317996004$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$317996004$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$317996004$--><span class="icon"><slot></slot></span>
        <!--?lit$317996004$-->
        <!--?lit$317996004$--><span class="touch"></span>
  </button></template>
        <!--?lit$317996004$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer" message="Toggle Gemini"><template shadowrootmode="open"><!----><!--?lit$317996004$--><!----><div><!--?lit$317996004$-->Toggle Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </span>
      <span class="right">
        <!--?lit$317996004$--><colab-execution-status><template shadowrootmode="open"><!----></template></colab-execution-status><!--?lit$317996004$--><!--?lit$317996004$--><!--?lit$317996004$--><colab-runtime-status><template shadowrootmode="open"><!----><span class="status-message"><!--?lit$317996004$-->Connecting to Python 3</span></template></colab-runtime-status>
      </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->data_object</md-icon>
        <!--?lit$317996004$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$317996004$-->terminal</md-icon>
        <!--?lit$317996004$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 663px; visibility: visible; left: 68px; top: 62px; display: none;"><!--?lit$317996004$--><div command="locate-in-drive" class="goog-menuitem" role="menuitem" id=":33" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Locate in Drive<!--?lit$317996004$--></div></div><div command="open-in-playground" class="goog-menuitem" role="menuitem" id=":34" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Open in playground mode<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":35" style="user-select: none;"></div><div command="new" class="goog-menuitem" role="menuitem" id=":36" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->New notebook in Drive<!--?lit$317996004$--></div></div><div command="open" class="goog-menuitem" role="menuitem" id=":37" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Open notebook<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class="goog-menuitem" role="menuitem" id=":38" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Upload notebook<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":39" style="user-select: none;"></div><div command="rename" class="goog-menuitem" role="menuitem" id=":3a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Rename<!--?lit$317996004$--></div></div><div command="move-notebook" class="goog-menuitem" role="menuitem" id=":3b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Move<!--?lit$317996004$--></div></div><div command="trash" class="goog-menuitem" role="menuitem" id=":3c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Move to trash<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3d" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":3e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Save a copy in Drive<!--?lit$317996004$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":3f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Save a copy as a GitHub Gist<!--?lit$317996004$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":3g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Save a copy in GitHub<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3h" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":3i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Save<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":3j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Save and pin revision<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":3k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Revision history<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3l" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$317996004$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":3p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Print<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$317996004$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":3n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Download .ipynb<!--?lit$317996004$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":3o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Download .py<!--?lit$317996004$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$317996004$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":3r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Undo<!--?lit$317996004$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":3s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Redo<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3t" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":3u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Select all cells<!--?lit$317996004$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":3v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Cut cell or selection<!--?lit$317996004$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":3w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Copy cell or selection<!--?lit$317996004$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":3x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Paste<!--?lit$317996004$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":3y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Delete selected cells<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":3z" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":40" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Find and replace<!--?lit$317996004$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":41" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Find next<!--?lit$317996004$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":42" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Find previous<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":43" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":44" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Notebook settings<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":45" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":46" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Clear all outputs<!--?lit$317996004$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 663px; visibility: visible; left: 148.338px; top: 62px; display: none;"><!--?lit$317996004$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":48" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----> </div><!--?lit$317996004$-->Table of contents<!--?lit$317996004$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":49" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Notebook info<!--?lit$317996004$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":4a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Executed code history<!--?lit$317996004$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$317996004$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4f" style="user-select: none;"></div><div command="collapse-sections" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":4g" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Collapse sections<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+]</span></div></div><div command="expand-sections" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":4h" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Expand sections<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+[</span></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":4i" style="user-select: none; display: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Save collapsed section layout<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4j" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":4k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Show/hide code<!--?lit$317996004$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":4l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Show/hide output<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+M O</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4m" style="user-select: none;"></div><div command="focus-next-tab" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":4n" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Focus next tab<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+Shift+]</span></div></div><div command="focus-previous-tab" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":4o" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Focus previous tab<!--?lit$317996004$--><span class="goog-menuitem-accel">Ctrl+Shift+[</span></div></div><div command="move-tab-to-next" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":4p" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Move tab to next pane<!--?lit$317996004$--></div></div><div command="move-tab-to-prev" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":4q" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Move tab to previous pane<!--?lit$317996004$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$317996004$--><div command="hide-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option" role="menuitemradio" id=":4c" aria-checked="false" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"></div><!--?lit$317996004$-->Hide comments<!--?lit$317996004$--></div></div><div command="show-minimized-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option" role="menuitemradio" id=":4d" aria-checked="false" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"></div><!--?lit$317996004$-->Minimize comments<!--?lit$317996004$--></div></div><div command="show-expanded-sidebar-comments" class="goog-menuitem goog-option-selectable goog-option goog-option-selected" role="menuitemradio" id=":4e" aria-checked="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$317996004$-->Expand comments<!--?lit$317996004$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$317996004$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":4s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Code cell<!--?lit$317996004$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":4t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Text cell<!--?lit$317996004$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":4u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Section header cell<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4v" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":4w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Scratch code cell<!--?lit$317996004$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":4x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Code snippets<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4y" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":4z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Add a form field<!--?lit$317996004$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$317996004$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":51" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Run all<!--?lit$317996004$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":52" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Run before<!--?lit$317996004$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":53" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Run the focused cell<!--?lit$317996004$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":54" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Run selection<!--?lit$317996004$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":55" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Run cell and below<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":56" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":57" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Interrupt execution<!--?lit$317996004$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":58" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Restart session<!--?lit$317996004$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":59" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Restart session and run all<!--?lit$317996004$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":5a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Disconnect and delete runtime<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5b" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":5c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Change runtime type<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5d" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":5e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Manage sessions<!--?lit$317996004$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":5f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->View resources<!--?lit$317996004$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":5g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->View runtime logs<!--?lit$317996004$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$317996004$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":5i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Command palette<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5j" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":5k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Settings<!--?lit$317996004$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":5l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Keyboard shortcuts<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5m" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":5n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Diff notebooks<!--?lit$317996004$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$317996004$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$317996004$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":5p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Frequently asked questions<!--?lit$317996004$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":5q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->View release notes<!--?lit$317996004$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":5r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Search code snippets<!--?lit$317996004$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5s" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":5t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Report a bug<!--?lit$317996004$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":5u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Report Drive abuse<!--?lit$317996004$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":5v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->Send feedback<!--?lit$317996004$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":5w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$317996004$-->View terms of service<!--?lit$317996004$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$317996004$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$317996004$--><button id="button" class="button">
      <!--?lit$317996004$-->
      <span class="touch"></span>
      <!--?lit$317996004$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$317996004$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$317996004$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><div><div class="grecaptcha-badge" data-style="none" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-zcxtt6lswzyz" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./bankapp_files/anchor(1).html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100001" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div></div></body></html>