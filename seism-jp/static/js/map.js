// TODO change here.
const lonlatList = [
  [131.952623346905, 31.68851745137],
  [137.89692002991, 36.24146762918334],
  [136.85702358215002, 35.86815606129001],
  [137.55363293263667, 35.85650280896],
  [142.95124964736502, 41.68430707853667],
  [139.33530832701834, 32.45356457715334],
  [135.38057161831333, 33.86834417278334],
  [130.53438684893666, 32.143444019346674],
  [141.21146580800502, 40.12777651001],
  [142.96291519173667, 41.68764025911667],
  [139.681804792055, 35.52490878325667],
  [135.57548483332835, 35.40151692159667],
  [140.89320893798669, 39.041220502970006],
  [142.37644011489002, 38.584628581736666],
  [135.92715329546002, 34.72826174277],
  [140.65665031779, 37.12142171382333],
  [130.59770203224, 32.4234151794],
  [135.08724852594003, 34.17497291867667],
  [140.0400049362733, 37.771341426856665],
  [137.05046232409333, 33.230108274079996],
  [136.30042263217334, 35.44485828183001],
  [142.32968931425333, 40.49608998066667],
  [130.93769505183002, 31.961803825743328],
  [137.49875865667167, 33.22511663852333],
  [142.3930875961467, 38.97125418547],
  [141.63648905972, 38.85625327029334],
  [130.92936287090168, 31.95180474971],
  [137.43200882632502, 35.15157608392333],
  [142.22303756717665, 40.36443553292333],
  [141.341589136455, 37.21475702799667],
  [129.03114398187336, 32.8900045758],
  [131.01431299690668, 32.88170677065],
  [136.90704206535, 35.37654285157334],
  [131.27930250001168, 32.63173813611],
  [134.2306279087333, 34.719899670100006],
  [129.01801716199003, 28.42881485153],
  [130.312766136205, 31.545170806576667],
  [123.50532858667667, 24.369152783676665],
  [143.02283240493665, 43.37746056145667],
  [129.02801610137, 28.433814491419998],
  [129.02801617810002, 28.43214800300333],
  [130.33109825400336, 31.53850517308333],
  [130.86608881487837, 30.77859579832333],
  [130.30943307968167, 31.545170748363333],
  [130.31443266446666, 31.545170835683333],
  [129.72445948486668, 32.02677568434],
  [129.70612767398836, 32.026775364166674],
  [130.92769618918, 31.955137697436665],
  [130.06942546393168, 32.143435898586674],
  [135.20890616326167, 34.15164420563001],
  [149.49553410227, 45.42068841058334],
  [135.61720873330003, 34.08332531168],
  [132.26088787632332, 32.626755814686675],
  [132.252555465205, 32.62175620390334],
  [130.55601074251834, 33.03334921223334],
  [137.53696005375, 36.021484871143336],
  [137.54363399325666, 35.85150316907001],
  [135.612173699255, 34.85324287286],
  [150.170527999475, 44.335816239533344],
  [136.92706618577003, 34.816603092853335],
  [128.1497659125617, 28.212156192789998],
  [132.00929873555168, 31.39688296808],
  [140.11837949063167, 36.73478699970334],
  [131.03768705445, 31.955139618476668],
  [134.792249390785, 34.68824619913],
  [131.73260708786503, 32.43843339679001],
  [140.60334036572667, 36.70979814349333],
  [130.58770002366, 32.48507507617667],
  [138.35360248460665, 35.07493371274333],
  [123.80697534294835, 24.257503328066665],
  [123.80697526621834, 24.25916981648333],
  [139.68350370037666, 34.82165070053001],
  [142.151399026895, 39.88281912892],
  [140.56500829745832, 36.75145968445667],
  [141.62982701336333, 38.76792926778334],
  [136.36706304554, 35.894811318596666],
  [134.96727936166, 33.721685973663334],
  [139.60665456781, 38.92287735504001],
  [136.91037443130332, 35.39154130553667],
  [131.70593925955833, 32.511758421416665],
  [140.53667478492, 36.80645330739333],
  [140.881539326925, 39.126211208473336],
  [140.54000776471332, 36.80811985402334],
  [140.52834175996168, 36.81478560394334],
  [140.53834123645166, 36.80811982491667],
  [150.21385995944834, 44.28748883222333],
  [140.53500817992833, 36.808119766703335],
  [141.021687299305, 35.659917746766666],
  [141.74641884791, 40.182779971],
  [121.67216207754333, 24.052487967176663],
  [140.581672505855, 36.774790813356674],
  [129.80125482970334, 29.093757409913334],
  [130.70768223203999, 32.655058990356665],
  [142.8546610626783, 40.16280146593333],
  [141.33325933415668, 37.153096811046666],
  [131.53095709147334, 32.4400963633],
  [138.12691735024, 35.884843124736676],
  [140.431727010345, 35.861552541423336],
  [136.37541279763835, 35.52318454721334],
  [144.61435085825835, 43.72578443740667],
  [130.3443961050567, 32.28509221660333],
  [141.54156592907498, 37.35807852463],
  [131.232736541945, 30.528628939289995],
  [131.95597029155834, 31.386883106166664],
  [138.72353469810665, 35.87985407967333],
  [130.38445086794667, 31.02356118374666],
  [137.581954475295, 36.061481379023334],
  [129.7344588078967, 32.02344288214667],
  [137.41700615873998, 35.23656673121334],
  [130.06942546393168, 32.143435898586674],
  [129.0196836135217, 28.430481369053332],
  [130.70102072279337, 32.55506956893001],
  [141.50454819836833, 45.048921927200006],
  [135.21391656697668, 33.9166694262],
  [141.34827404835164, 36.806467482340004],
  [142.47308340806669, 38.91792795325667],
  [138.13025048349334, 35.88317669453334],
  [138.6833554791567, 39.84442932436333],
  [139.50848170942166, 35.61489613066333],
  [139.5051488063583, 35.611563095616674],
  [139.75678828201, 35.74821954089],
  [129.78609839519834, 32.51839084420333],
  [138.03525645432833, 35.92483724587],
  [142.1179523691717, 42.404215521203334],
  [141.02999185743334, 36.2698526528],
  [137.36201732488502, 35.09324776686001],
  [141.82654287566, 37.34475159453667],
  [141.15994423144335, 37.06976936312001],
  [128.17809812069, 28.185492872936667],
  [141.56456055676833, 44.67229659287334],
  [128.15809878405997, 28.20715687307333],
  [130.622744843215, 31.44851989225],
  [140.54000776471332, 36.80811985402334],
  [135.592218175455, 33.92334198708001],
  [144.03631039689, 38.40800979981],
  [123.76031285854168, 24.25083655941333],
  [139.951571900055, 40.096091225453335],
  [142.72617057802, 43.807409391970005],
  [141.47290487849665, 44.59896950167333],
  [137.27702461373002, 35.08824681717],
  [129.56961545798166, 28.918772080336666],
  [144.51275701076668, 42.32759888031667],
  [135.19223727433499, 34.22996887014667],
  [141.7898402750633, 38.19132706985667],
  [142.17643378122, 39.08290512552],
  [129.66128279921332, 28.73879293220333],
  [140.53834131318166, 36.806453336500006],
  [130.59627098834835, 27.30896219954333],
  [131.9291833782917, 34.04659815346001],
  [139.11014976539334, 36.30314889025333],
  [135.7371712988, 34.679930260526675],
  [140.20001766086332, 37.20640464784667],
  [135.57381807487664, 35.40651635774],
  [138.13354149197667, 36.796412405080005],
  [147.940750629605, 43.52253094748001],
  [139.95014231403334, 34.94997496568],
  [141.621525754625, 38.086335359833335],
  [142.38975845285336, 38.88626321800667],
  [133.30567740762834, 35.31315339223334],
  [128.82470195534665, 28.383816287906665],
  [129.71612707374834, 32.021776073556666],
  [134.23727084932, 35.22317928836],
  [140.92002078850334, 35.83989672026],
  [137.52696226532, 35.99148790500333],
  [131.232635258345, 32.728393649290005],
  [139.22683122058, 35.771541122803335],
  [133.07575420847837, 34.059950086179995],
  [142.21811425201167, 38.707945959436664],
  [130.302923802755, 28.138868308270002],
  [141.52789593752166, 44.693960301943335],
  [140.90502088319832, 35.86489378455],
  [136.06713207818999, 34.93657523981333],
  [135.67383194554668, 34.92490295172333],
  [135.38389446974665, 34.08998719041333],
  [140.38836420491168, 36.57980829223334],
  [142.10808072486168, 39.634511598063334],
  [142.2032075736567, 36.708159597476666],
  [137.52696218859, 35.993154393420006],
  [131.53762328125, 32.43842999131001],
  [140.8200070712933, 36.318177149443336],
  [136.92206000220503, 34.95992100936667],
  [139.37002259373335, 38.596241492226675],
  [130.502852869315, 29.31874560007],
  [132.5707441989833, 35.18815392494334],
  [140.53000821149334, 36.81645212146667],
  [131.49256640148502, 33.754955054596664],
  [131.09774468355, 30.59528611831666],
  [141.85320249385666, 37.44974083049333],
  [132.442481142045, 33.89329018398],
  [129.7177930649, 32.03344152158],
  [137.77699107215, 34.914940753836675],
  [140.93487007281834, 39.086216417886675],
  [136.84540323174835, 34.88326120329334],
  [136.85040258634334, 34.888260755863335],
  [140.85647349695003, 40.60105302062333],
  [142.70304021495667, 39.441209332810004],
  [140.811674429985, 36.31817700391],
  [136.262059104605, 36.16978007362666],
  [131.342703160535, 31.055241199996665],
  [140.89154532546502, 38.977893914030005],
  [141.58826532061167, 36.56316436486667],
  [136.55710773061, 34.58162176442334],
  [133.91404493305666, 33.47336080416667],
  [138.45872167400168, 32.29689935588001],
  [142.50294771349667, 41.810952368509994],
  [134.56730774487002, 33.826667758313334],
  [136.51206243707497, 35.64650707679333],
  [129.75779028028998, 32.02177680122333],
  [140.54667372430004, 36.81145294728333],
  [145.09601473993, 42.91754596715],
  [130.70102095298336, 32.55007010368001],
  [130.05942652455167, 32.138436258696665],
  [137.2470298673, 35.028252710249994],
  [130.05775976610002, 32.14343569484001],
  [124.04857275696, 25.325726623616664],
  [130.062759197425, 32.14676875899333],
  [133.082421088825, 34.04328531844],
  [130.06775908913, 32.14010289264667],
  [142.2297538616433, 39.274552224850005],
  [134.28735647127002, 33.273388714060005],
  [142.2297537849133, 39.276218713266665],
  [143.591138261775, 42.94918296374667],
  [142.18644238858, 38.87792722491],
  [137.66700749622999, 34.75662243321333],
  [132.59583128316834, 33.251694821376674],
  [141.37320122721667, 38.34297023910667],
  [140.24837069002166, 36.69146057119001],
  [129.46633045189836, 28.05552927589],
  [142.60965815902335, 40.66774317750333],
  [142.16313025214666, 38.459638224833334],
  [141.02498406253832, 36.448166826063336],
  [141.26662996991, 36.463169442280005],
  [130.92445582249667, 29.94201963189],
  [139.75343312724667, 36.22816814667667],
  [137.56862263285166, 36.05314870408667],
  [139.45501461431834, 38.616240837666666],
  [135.57381815160664, 35.404849869323336],
  [138.84854795057166, 35.366577830340006],
  [135.41888366005165, 34.26163610857],
  [144.57939266687336, 42.880874198916665],
  [131.532623696465, 32.438429903990006],
  [141.35658766062002, 37.219756755206674],
  [133.31067607165335, 35.333151340553336],
  [129.5196599701117, 28.042198299969996],
  [141.76651233225002, 38.11633468361334],
  [140.05694053868, 31.900303026006668],
  [130.92103038305336, 31.94847162734333],
  [141.95649770503002, 38.091340675523334],
  [141.81654355262998, 37.34808439673],
  [129.72445925467667, 32.031775149590004],
  [130.73601735590833, 32.56506911067],
  [131.66095627078334, 32.223455139453336],
  [139.091854784915, 35.50323413008],
  [141.0482679623317, 37.479723563473335],
  [141.01001937630332, 35.70824570710333],
  [129.73112544445334, 32.0301087776],
  [141.17994226366332, 37.07643566606667],
  [137.98189946677502, 36.53477107495667],
  [143.02116587667498, 43.37746053235001],
  [135.3855898484883, 33.46338757485334],
  [130.952786189105, 29.955352034036665],
  [129.90128013314336, 28.36383722981333],
  [137.56862247939165, 36.05648168092001],
  [140.551673922925, 36.79812112727001],
  [140.95669538265003, 35.601589517023335],
  [141.82642808758, 39.837818265870006],
  [140.84503476645833, 35.67158008037667],
  [139.90852921218166, 33.861757301930005],
  [142.00957585576333, 43.53742575260333],
  [129.4646639236367, 28.055529246783333],
  [140.53334142147668, 36.81311920284667],
  [137.05705193733, 34.89159734192334],
  [142.34475789290832, 38.97958578346],
  [135.57884052520168, 34.909902896893335],
  [142.31814062967166, 37.95469494150334],
  [142.1081377352517, 38.396310704479994],
  [142.20479414925836, 38.44464055675001],
  [139.39175882003502, 37.04640764311334],
  [129.52132764932335, 28.017201002826663],
  [130.03942810868165, 32.14010239783333],
  [129.9777941858, 31.540165490886665],
  [139.45334685837668, 38.64290462322667],
  [131.0677381207, 30.791931227563335],
  [140.84003364707334, 35.704909761390006],
  [123.67864883030002, 24.340825507686663],
  [132.10757157313003, 32.53342978554001],
  [139.09694437399, 33.54844330465],
  [130.66768294494, 32.711718897963344],
  [129.442991843615, 28.212178779563327],
  [130.92269691131503, 31.94847165645],
  [139.51681511803, 35.59823139203],
  [140.53667470819, 36.80811979581],
  [135.39726030358, 33.36006549676667],
  [142.10474413875832, 39.71117000701667],
  [139.37668870678002, 38.59624160865334],
  [140.48838828067167, 35.876551926800005],
  [140.74997804888332, 37.07476166813],
  [141.75486727478832, 37.66804909578333],
  [137.9535847530867, 36.18147503581],
  [132.43749805421, 33.53499508707667],
  [139.09010592536333, 37.29137617205667],
  [138.35692203665, 35.36823573229],
  [136.26048603348332, 34.13999715302],
  [129.28964799435167, 28.717122092],
  [135.19391040137666, 34.08665089542001],
  [135.36722949405, 34.08332094568],
  [140.56167385979498, 36.78145641774334],
  [135.29554460884833, 34.608263545343334],
  [143.58811465734166, 36.22823512111667],
  [130.6177451817, 31.450186293346665],
  [139.78684817221, 34.39336498206],
  [140.63332314227668, 37.029764443413335],
  [132.15087544992335, 33.09503713873001],
  [129.70779420225003, 32.02677539327334],
  [140.971626000765, 37.081431492983334],
  [137.57361262638665, 36.26145984349],
  [137.56027932607336, 36.284790448470005],
  [144.26107425939497, 43.13084190204333],
  [131.00426011633667, 34.048248487676666],
  [141.09827140645166, 37.31474208342334],
  [139.49501152278836, 38.61124207097667],
  [128.09977259680167, 28.157161201839997],
  [123.73696910934832, 24.519140787003334],
  [129.73279243309503, 32.02010987620667],
  [146.49249659639668, 44.412410468286666],
  [139.45001533645336, 38.60957479668],
  [124.17525729494668, 24.709128121556663],
  [132.39585441381834, 33.11003981316001],
  [139.18337365359668, 38.54791006819667],
  [139.191707138935, 38.529578841146666],
  [122.47544036262667, 23.79919575725667],
  [122.483774001425, 23.777531553373333],
  [141.901534729185, 37.38641511475333],
  [141.03665328995, 36.371508562643335],
  [138.71860616530165, 34.33668571852001],
  [122.49044057485166, 23.767532739299998],
  [140.63505527468834, 35.60491687627],
  [129.50631930371833, 28.22551179295],
  [142.38809468687168, 38.826269605899995],
  [135.4888825275717, 34.159981537633335],
  [137.44029573655334, 36.14480332579],
  [138.26692490672, 35.46822346553],
  [139.36989368733333, 41.39594203222667],
  [150.35380989169832, 45.12240197393333],
  [141.941287559525, 42.68251600148],
  [135.24042894030336, 37.21964993374001],
  [142.35308316813666, 39.13956881699333],
  [136.18382335481667, 34.191656955030005],
  [136.23048791093333, 34.153328536433335],
  [132.25755543364, 32.61342384914],
  [138.06856369364166, 36.43145030667],
  [128.15309942946502, 28.202157320503332],
  [140.73332228078667, 36.86811681339667],
  [140.52500824305835, 36.82478447623],
  [137.68867297747167, 34.74329090426667],
  [125.25349793431499, 24.777472978653332],
  [129.72112704218335, 32.01344371879333],
  [140.40677543134, 34.85499310115667],
  [140.5483397921817, 36.821451906890005],
  [133.84062906639335, 35.39815364472334],
  [133.8439622763767, 35.39482072610334],
  [135.22391573654667, 33.91666960084],
  [142.33641727168, 39.15290043326],
  [140.5483394085317, 36.82978434897334],
  [139.24839633898165, 37.93797644285667],
  [129.15638051863834, 27.527247033966663],
  [130.9293629476317, 31.950138261293333],
  [131.51101967595332, 31.116904211186664],
  [133.45410185495666, 33.066729597060004],
  [139.781773392025, 36.02652354307333],
  [133.52737822647998, 34.17161269800334],
  [139.43836329656168, 38.312939654766666],
  [129.53631075075833, 28.357164901786664],
  [140.28339625034667, 36.07319397984667],
  [129.50611159560833, 32.73669593686667],
  [137.35033796911333, 35.38988250127999],
  [139.45677060976, 36.67311537294],
  [129.71612661336835, 32.031775004056676],
  [140.5483394852617, 36.828117860556674],
  [142.10313346993667, 38.497966410576666],
  [130.62936422769167, 32.46341145442667],
  [135.20224971819502, 33.94166654870334],
  [143.001236364345, 41.882620073320005],
  [140.94835123184166, 35.85156263399001],
  [131.07608794952836, 30.41863796776333],
  [136.302089160435, 35.444858310936674],
  [141.20150208769502, 39.35785868687],
  [131.77763542406998, 31.74184202450333],
  [139.98667687593002, 37.75300912286],
  [131.7609702181833, 31.74017524502],
  [131.242634504645, 32.72672733551334],
  [139.38511549579835, 36.55146046693667],
  [135.162246748055, 34.078317900310005],
  [128.41647603857834, 26.787313253606666],
  [123.0986656894, 25.020742652566664],
  [142.08647570686, 38.33465025467667],
  [130.90936606636166, 31.918474632096665],
  [130.93936403545166, 31.90847622551667],
  [130.91436588133666, 31.913475254166666],
  [130.68268423138502, 32.656725042173335],
  [129.10804997137004, 27.55391000454],
  [133.6357398542683, 33.36170121943667],
  [144.14794622929168, 38.87629499504],
  [135.43555001688836, 34.23830556180333],
  [132.15587495797834, 33.09670371446666],
  [140.621769546975, 34.59502466291667],
  [130.05775999629, 32.13843622959],
  [138.04024276482332, 36.21313982927334],
  [140.11341259282668, 36.02486284688334],
  [146.40922665659335, 43.185873538286664],
  [141.00836136507166, 35.523265463746675],
  [141.16662131687997, 36.831461635963336],
  [141.71487903680833, 37.48473467139],
  [129.95941495578168, 32.57005501221334],
  [142.23473234567834, 39.73283662675333],
  [132.42421224976667, 32.52676936214],
  [129.72445956159666, 32.025109195923335],
  [142.31977684958332, 38.61295789519334],
  [141.69821720704164, 37.40974240157334],
  [140.43656975901, 39.267854952410005],
  [129.90458441591667, 28.988770444276664],
  [141.84986007627333, 37.65305235911333],
  [131.24930061769166, 32.72672745194001],
  [140.4800105988533, 36.85478048185],
  [140.98997146958337, 36.78479687499],
  [132.42095998993335, 30.771957001176666],
  [129.73112544445334, 32.0301087776],
  [148.37070195374503, 43.804174999416674],
  [128.60804345989, 28.59712302137333],
  [141.95480209609835, 38.72293975633333],
  [140.871547600165, 38.96456165741667],
  [140.53500403650833, 36.89811014120334],
  [142.10975707456336, 39.421201109836666],
  [135.622173482665, 34.83991114016666],
  [131.3144031790067, 30.38197938485],
  [132.70246553580503, 33.76330862812],
  [142.35478529911833, 38.36631822076667],
  [139.72506945981834, 36.938091717363335],
  [129.952749072925, 32.565055430536674],
  [137.55862384693168, 36.04481608736334],
  [136.18381522143667, 34.36830472719667],
  [130.31940278493167, 32.18510247500333],
  [129.53631665896833, 28.228845293703333],
  [131.53262377319498, 32.43676341557333],
  [123.91861025459, 24.745786384296668],
  [136.57706210346004, 35.536519976453334],
  [142.32145573137498, 38.34465328921667],
  [122.99871911094, 24.040845717166665],
  [130.56771219652998, 32.25676581381333],
  [140.36672496533, 36.02320078268001],
  [140.871542996365, 39.06455096241667],
  [140.86487726696834, 39.05621840390667],
  [131.24932072095166, 32.29010748677334],
  [137.90525428254836, 36.20647151796667],
  [135.29387831077665, 34.603264050986674],
  [131.24096812984334, 32.72339432957333],
  [131.152741957705, 30.555291356836666],
  [140.00008368358334, 36.13318261471334],
  [131.24596733097832, 32.73172685897667],
  [129.46133478034335, 27.970538279319996],
  [131.55759806428, 32.95004228450667],
  [131.13090728681334, 34.24322984453333],
  [140.841680148805, 36.13986326724667],
  [140.58167035741502, 36.821452489023336],
  [136.90370785787667, 35.40154011961],
  [136.92376006147668, 34.23166560039],
  [138.06523063711833, 36.43145024845667],
  [135.54384143672664, 34.95323098448667],
  [131.2560031774883, 31.935145570449997],
  [132.33920588067167, 32.81840335061666],
  [137.51196205309498, 36.023150922960006],
  [123.473634778465, 25.015749736316668],
  [131.092746096255, 30.573621681579997],
  [130.49771133403001, 32.40174908358333],
  [140.56667620686, 36.72146292206333],
  [130.50767950468, 33.075010578556665],
  [138.85021447883332, 35.36657785944667],
  [141.64816465572167, 38.64127646829],
  [138.85354745862665, 35.36824440607667],
];

function init() {
  const map = new OpenLayers.Map('basicMap');
  const mapnik = new OpenLayers.Layer.OSM();
  const fromProjection = new OpenLayers.Projection('EPSG:4326');
  const toProjection = new OpenLayers.Projection('EPSG:900913');
  // japan center position.
  const position = new OpenLayers.LonLat(138.2529, 36.2048).transform(
    fromProjection,
    toProjection
  );
  // all view japan.
  const zoom = 6;
  map.addLayer(mapnik);
  map.setCenter(position, zoom);

  // add marker.
  const markers = new OpenLayers.Layer.Markers('Markers');
  map.addLayer(markers);
  for (let i = 0; i < lonlatList.length; i++) {
    const lonlat = lonlatList[i];
    const pos = new OpenLayers.LonLat(lonlat[0], lonlat[1]).transform(
      fromProjection,
      toProjection
    );
    markers.addMarker(new OpenLayers.Marker(pos));
  }
}