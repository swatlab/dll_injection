query = '''
query_format=advanced&
j1=OR&
f1=OP&
  j2=AND&
  f2=OP&
    f3=product&o3=equals&v3=External%20Software%20Affecting%20Firefox&
    f4=component&o4=equals&v4=Other&
  f5=CP&
  f6=status_whiteboard&o6=substring&v7=%5BAV&
  f8=longdesc&o8=substring&v8=caused%20by%20antivirus&
  j12=AND&
  f12=OP&
    f13=short_desc&o13=substring&v13=.dll&
    f14=short_desc&o14=notsubstring&v14=mozglue.dll&
    f15=short_desc&o15=notsubstring&v15=xul.dll&
    f16=short_desc&o16=notsubstring&v16=nss3.dll&
    f17=short_desc&o17=notsubstring&v17=browsercomps.dll&
    f18=short_desc&o18=notsubstring&v18=nvd3d&
    f19=short_desc&o19=notsubstring&v19=nvwgf2um&
    f20=short_desc&o20=notsubstring&v20=nvoglv&
    f21=short_desc&o21=notsubstring&v21=nvappfilter&
    f22=short_desc&o22=notsubstring&v22=nvlsp&
    f23=short_desc&o23=notsubstring&v23=atidxx&
    f24=short_desc&o24=notsubstring&v24=atiu9&
    f25=short_desc&o25=notsubstring&v25=atiumd&
    f26=short_desc&o26=notsubstring&v26=aticfx&
    f27=short_desc&o27=notsubstring&v27=igd10&
    f28=short_desc&o28=notsubstring&v28=igdum&
    f29=short_desc&o29=notsubstring&v29=ntdll.dll&
    f30=short_desc&o30=notsubstring&v30=user32.dll&
    f31=short_desc&o31=notsubstring&v31=PSAPI.dll&
    f32=short_desc&o32=notsubstring&v32=d3d11.dll&
    f33=short_desc&o33=notsubstring&v33=kernelbase.dll&
    f34=short_desc&o34=notsubstring&v34=vcruntime140.dll&
    f35=short_desc&o35=notsubstring&v35=msvcr120.dll&
    f36=short_desc&o36=notsubstring&v36=ucrtbase.dll&
    f37=short_desc&o37=notsubstring&v37=msmpeg2vdec.dll&
    f38=short_desc&o38=notsubstring&v38=widevinecdm.dll&
    f39=short_desc&o39=notsubstring&v39=eme-adobe.dll&
    f40=short_desc&o40=notsubstring&v40=eme-adobe.dll&
    f41=short_desc&o41=notsubstring&v41=openh264.dll&
    f42=short_desc&o42=notsubstring&v42=openh264.dll&
    f43=short_desc&o43=notsubstring&v43=npswf&
    f44=short_desc&o44=notsubstring&v44=npsf_abn&
    f45=short_desc&o45=notsubstring&v45=npsf_cef&
    f46=short_desc&o46=notsubstring&v46=npjp2&
    f47=short_desc&o47=notsubstring&v47=lgpllibs.dll&
    f48=short_desc&o48=notsubstring&v48=atiux&
    f49=short_desc&o49=notsubstring&v49=d3dcompiler&
    f50=short_desc&o50=notsubstring&v50=d3d10warp&
    f51=short_desc&o51=notsubstring&v51=dgapi&
    f52=short_desc&o52=notsubstring&v52=mspdb140&
    f53=short_desc&o53=notsubstring&v53=libGLES&
    f54=short_desc&o54=notsubstring&v54=libGLES&
    f55=short_desc&o55=notsubstring&v55=libovrrt&
    f56=short_desc&o56=notsubstring&v56=igd11dxva&
    f57=short_desc&o57=notsubstring&v57=pgort140&
    f58=short_desc&o58=notsubstring&v58=ole32&
    f59=short_desc&o59=notsubstring&v59=nvumdshim&
  f60=CP&
  f61=short_desc&o61=substring&v61=virus&
  f62=short_desc&o62=substring&v62=malware&
  f63=short_desc&o63=substring&v63=adware&
f64=CP&

j65=AND_G&
f65=OP&
  f66=creation_ts&o66=greaterthan&v66=2015-07-02&
  f67=creation_ts&o67=lessthan&v67=2017-08-25&
f68=CP&

product=Core&product=External%20Software%20Affecting%20Firefox&product=Firefox&product=NSPR&product=NSS&product=Toolkit
'''

query = query.replace('\n', '').replace(' ', '')

print('https://bugzilla.mozilla.org/buglist.cgi?' + query)
print('\n')
print('https://bugzilla.mozilla.org/rest/bug?' + query + '&count_only=true')
