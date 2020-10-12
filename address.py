import random
import itertools

arr = {'alley': ['allee', 'alley', 'ally', 'aly'], 'anex': ['anex', 'annex', 'annx', 'anx'], 'arcade': ['arc', 'arcade'], 'avenue': ['av', 'ave', 'aven', 'avenu', 'avenue', 'avn', 'avnue'], 'bayou': ['bayoo', 'bayou', 'byu'], 'beach': ['bch', 'beach'], 'bend': ['bend', 'bnd'], 'bluff': ['blf', 'bluf', 'bluff'], 'bluffs': ['blfs', 'bluffs'], 'bottom': ['bot', 'bottm', 'bottom', 'btm'], 'boulevard': ['blvd', 'boul', 'boulevard', 'boulv'], 'branch': ['br', 'branch', 'brnch'], 'bridge': ['brdge', 'brg', 'bridge'], 'brook': ['brk', 'brook'], 'brooks': ['brks', 'brooks'], 'burg': ['bg', 'burg'], 'burgs': ['bgs', 'burgs'], 'bypass': ['byp', 'bypa', 'bypas', 'bypass', 'byps'], 'camp': ['camp', 'cmp', 'cp'], 'canyon': ['canyn', 'canyon', 'cnyn', 'cyn'], 'cape': ['cape', 'cpe'], 'causeway': ['causeway', 'causwa', 'cswy'], 'center': ['cen', 'cent', 'center', 'centr', 'centre', 'cnter', 'cntr', 'ctr'], 'centers': ['centers', 'ctrs'], 'circle': ['cir', 'circ', 'circl', 'circle', 'crcl', 'crcle'], 'circles': ['circles', 'cirs'], 'cliff': ['clf', 'cliff'], 'cliffs': ['clfs', 'cliffs'], 'club': ['clb', 'club'], 'common': ['cmn', 'common'], 'commons': ['cmns', 'commons'], 'corner': ['cor', 'corner'], 'corners': ['corners', 'cors'], 'course': ['course', 'crse'], 'court': ['court', 'ct'], 'courts': ['courts', 'cts'], 'cove': ['cove', 'cv'], 'coves': ['coves', 'cvs'], 'creek': ['creek', 'crk'], 'crescent': ['cres', 'crescent', 'crsent', 'crsnt'], 'crest': ['crest', 'crst'], 'crossing': ['crossing', 'crssng', 'xing'], 'crossroad': ['crossroad', 'xrd'], 'crossroads': ['crossroads', 'xrds'], 'curve': ['curv', 'curve'], 'dale': ['dale', 'dl'], 'dam': ['dam', 'dm'], 'divide': ['div', 'divide', 'dv', 'dvd'], 'drive': ['dr', 'driv', 'drive', 'drv'], 'drives': ['drives', 'drs'], 'estate': ['est', 'estate'], 'estates': ['estates', 'ests'], 'expressway': ['exp', 'expr', 'express', 'expressway', 'expw', 'expy'], 'extension': ['ext', 'extension', 'extn', 'extnsn'], 'extensions': ['exts'], 'fall': ['fall'], 'falls': ['falls', 'fls'], 'ferry': ['ferry', 'frry', 'fry'], 'field': ['field', 'fld'], 'fields': ['fields', 'flds'], 'flat': ['flat', 'flt'], 'flats': ['flats', 'flts'], 'ford': ['ford', 'frd'], 'fords': ['fords', 'frds'], 'forest': ['forest', 'forests', 'frst'], 'forge': ['forg', 'forge', 'frg'], 'forges': ['forges', 'frgs'], 'fork': ['fork', 'frk'], 'forks': ['forks', 'frks'], 'fort': ['fort', 'frt', 'ft'], 'freeway': ['freeway', 'freewy', 'frway', 'frwy', 'fwy'], 'garden': ['garden', 'gardn', 'gdn', 'grden', 'grdn'], 'gardens': ['gardens', 'gdns', 'grdns'], 'gateway': ['gateway', 'gatewy', 'gatway', 'gtway', 'gtwy'], 'glen': ['glen', 'gln'], 'glens': ['glens', 'glns'], 'green': ['green', 'grn'], 'greens': ['greens', 'grns'], 'grove': ['grov', 'grove', 'grv'], 'groves': ['groves', 'grvs'], 'harbor': ['harb', 'harbor', 'harbr', 'hbr', 'hrbor'], 'harbors': ['harbors', 'hbrs'], 'haven': ['haven', 'hvn'], 'heights': ['ht', 'hts'], 'highway': ['highway', 'highwy', 'hiway', 'hiwy', 'hway', 'hwy'], 'hill': ['hill', 'hl'], 'hills': ['hills', 'hls'], 'hollow': ['hllw', 'hollow', 'hollows', 'holw', 'holws'], 'inlet': ['inlt'], 'island': ['is', 'island', 'islnd'], 'islands': ['islands', 'islnds', 'iss'], 'isle': ['isle', 'isles'], 'junction': ['jct', 'jction', 'jctn', 'junction', 'junctn', 'juncton'], 'junctions': ['jctns', 'jcts', 'junctions'], 'key': ['key', 'ky'], 'keys': ['keys', 'kys'], 'knoll': ['knl', 'knol', 'knoll'], 'knolls': ['knls', 'knolls'], 'lake': ['lake', 'lk'], 'lakes': ['lakes', 'lks'], 'land': ['land'], 'landing': ['landing', 'lndg', 'lndng'], 'lane': ['lane', 'ln'], 'light': ['lgt', 'light'], 'lights': ['lgts', 'lights'], 'loaf': ['lf', 'loaf'], 'lock': ['lck', 'lock'], 'locks': ['lcks', 'locks'], 'lodge': ['ldg', 'ldge', 'lodg', 'lodge'], 'loop': ['loop', 'loops'], 'mall': ['mall'], 'manor': ['manor', 'mnr'], 'manors': ['manors', 'mnrs'], 'meadow': ['mdw', 'meadow'], 'meadows': ['mdw', 'mdws', 'meadows', 'medows'], 'mews': ['mews'], 'mill': ['mill', 'ml'], 'mills': ['mills', 'mls'], 'mission': ['missn', 'msn', 'mssn'], 'motorway': ['motorway', 'mtwy'], 'mount': ['mnt', 'mount', 'mt'], 'mountain': ['mntain', 'mntn', 'mountain', 'mountin', 'mtin', 'mtn'], 'mountains': ['mntns', 'mountains', 'mtns'], 'neck': ['nck', 'neck'], 'north': ['north', 'n'], 'orchard': ['orch', 'orchard', 'orchrd'], 'oval': ['oval', 'ovl'], 'overpass': ['opas', 'overpass'], 'park': ['park', 'prk'], 'parks': ['park', 'parks'], 'parkway': ['parkway', 'parkwy', 'pkway', 'pkwy', 'pky'], 'parkways': ['parkways', 'pkwy', 'pkwys'], 'pass': ['pass'], 'passage': ['passage', 'psge'], 'path': ['path', 'paths'], 'pike': ['pike', 'pikes'], 'pine': ['pine', 'pne'], 'pines': ['pines', 'pnes'], 'place': ['pl'], 'plain': ['plain', 'pln'], 'plains': ['plains', 'plns'], 'plaza': ['plaza', 'plz', 'plza'], 'point': ['point', 'pt'], 'points': ['points', 'pts'], 'port': ['port', 'prt'], 'ports': ['ports', 'prts'], 'prairie': ['pr', 'prairie', 'prr'], 'radial': ['rad', 'radial', 'radiel', 'radl'], 'ramp': ['ramp'], 'ranch': ['ranch', 'ranches', 'rnch', 'rnchs'], 'rapid': ['rapid', 'rpd'], 'rapids': ['rapids', 'rpds'], 'rest': ['rest', 'rst'], 'ridge': ['rdg', 'rdge', 'ridge'], 'ridges': ['rdgs', 'ridges'], 'river': ['riv', 'river', 'rivr', 'rvr'], 'road': ['rd', 'road'], 'roads': ['rds', 'roads'], 'route': ['route', 'rte'], 'row': ['row'], 'rue': ['rue'], 'run': ['run'], 'shoal': ['shl', 'shoal'], 'shoals': ['shls', 'shoals'], 'shore': ['shoar', 'shore', 'shr'], 'shores': ['shoars', 'shores', 'shrs'], 'skyway': ['skwy', 'skyway'], 'south': ['south', 's'], 'spring': ['spg', 'spng', 'spring', 'sprng'], 'springs': ['spgs', 'spngs', 'springs', 'sprngs'], 'spur': ['spur'], 'spurs': ['spur', 'spurs'], 'square': ['sq', 'sqr', 'sqre', 'squ', 'square'], 'squares': ['sqrs', 'sqs', 'squares'], 'station': ['sta', 'station', 'statn', 'stn'], 'stravenue': ['stra', 'strav', 'straven', 'stravenue', 'stravn', 'strvn', 'strvnue'], 'stream': ['stream', 'streme', 'strm'], 'street': ['st', 'str', 'street', 'strt'], 'streets': ['streets', 'sts'], 'summit': ['smt', 'sumit', 'sumitt', 'summit'], 'terrace': ['ter', 'terr', 'terrace'], 'throughway': ['throughway', 'trwy'], 'trace': ['trace', 'traces', 'trce'], 'track': ['track', 'tracks', 'trak', 'trk', 'trks'], 'trafficway': ['trafficway', 'trfy'], 'trail': ['trail', 'trails', 'trl', 'trls'], 'trailer': ['trailer', 'trlr', 'trlrs'], 'tunnel': ['tunel', 'tunl', 'tunls', 'tunnel', 'tunnels', 'tunnl'], 'turnpike': ['tpke', 'trnpk', 'turnpike', 'turnpk'], 'underpass': ['underpass', 'upas'], 'union': ['un', 'union'], 'unions': ['unions', 'uns'], 'valley': ['valley', 'vally', 'vlly', 'vly'], 'valleys': ['valleys', 'vlys'], 'viaduct': ['vdct', 'via', 'viadct', 'viaduct'], 'view': ['view', 'vw'], 'views': ['views', 'vws'], 'village': ['vill', 'villag', 'village', 'villg', 'villiage', 'vlg'], 'villages': ['villages', 'vlgs'], 'ville': ['ville', 'vl'], 'vista': ['vis', 'vist', 'vista', 'vst', 'vsta'], 'walk': ['walk'], 'walks': ['walk', 'walks'], 'wall': ['wall'], 'way': ['way', 'wy'], 'ways': ['ways'], 'well': ['well', 'wl'], 'wells': ['wells', 'wls']}


class Address:
    def __init__(self, address):
        self.parse_address(address.lower())
        
    def parse_address(self, addr):
        address = addr.split(' ')
        num = address[0]
        street_name = ' '.join(address[1:-1])
        street = address[-1]
        self.address = [num, street_name, street]

    def number(self):
        return self.address[0]

    def jigged_streets(self):
        return arr[self.address[2]]

    def jigged_street_names(self):
        new_street_names = []
        word = ""
        for num, letter in enumerate(self.address[1]):
            try:
                if letter in 'aeiou' and self.address[1][num-1] != " " and self.address[1][num+1] != " ":
                    new_street_names.append(word + self.address[1][len(word)+1:])
            except:
                pass
            word = word + letter
        new_street_names.append(self.address[1])
        return new_street_names

    @staticmethod
    def camel_case(string):
        new_arr = []
        array = string.split(' ')
        for word in array:
            if word.isalpha():
                word = word[0].upper() + word[1:]
            new_arr.append(word)
        return ' '.join(new_arr)

    def get_random_jigged(self):
        all_jigged = self.get_all_jigged()
        return all_jigged[random.randint(0, len(all_jigged)-1)]

    def get_all_jigged(self):
        num = self.number()
        combined = []
        for street_name in self.jigged_street_names():
            for street in self.jigged_streets():
                combined.append(self.camel_case('{} {} {}'.format(num, street_name, street)))
        return combined

addr = Address('23 E Testing Mountain Alley')
print(addr.get_random_jigged())
print(addr.get_all_jigged())
print("Number of jigged addresses = {}".format(len(addr.get_all_jigged())))
