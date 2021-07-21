#All the human chosen parameters of the analysis

# QC measures 
#!!! None of this parameters are really chosen in our analysis and are just sloppy bounds of the QC in Pijuan
MIN_COUNTS = 5000
MAX_COUNTS = 10E8
MIN_GENES = 0
MAX_GENES = 10E8
MIN_CELLS = 1
MAX_CELLS = 10E8
MIN_MT_FRACTION = 0
MAX_MT_FRACTION = 1

# HVGs
HVG_METHOD = "seurat"
N_HVG = None

# PCs
USE_HVGs = True
N_PCS = 50

## Neighbours
METRIC = "correlation"
N_NEIGBOURS = 25

#SAMPLE PARAMETERS
##HVGs
RECOMPUTE_HVGS = False
##PCs
RECOMPUTE_PCS = True
##Doublets
MAX_N_COUNTS = 39000
DOUBLET_SCORE_MAX_THRESHOLD = 0.15
DOUBLET_LOUVAIN_RESOLUTION = 1  
##Stripped
STRIPPED = 0.0022
##Cluster threshold
CLUSTER_THRESHOLD = 0.25
##Remove outliers
DISCONNECTION_DISTANCE = 7
MIN_CLUSTER_SIZE = 15

#SAVING PARAMETERS
SAVING_VERSION = ""

#EXCLUDE FROM HVGs GENES
sex_related = ["Xist"]
s_genes_list = \
    ['Mcm5', 'Pcna', 'Tyms', 'Fen1', 'Mcm2', 'Mcm4', 'Rrm1', 'Ung', 'Gins2',
     'Mcm6', 'Cdca7', 'Dtl', 'Prim1', 'Uhrf1', 'Mlf1ip', 'Hells', 'Rfc2',
     'Rpa2', 'Nasp', 'Rad51ap1', 'Gmnn', 'Wdr76', 'Slbp', 'Ccne2', 'Ubr7',
     'Pold3', 'Msh2', 'Atad2', 'Rad51', 'Rrm2', 'Cdc45', 'Cdc6', 'Exo1', 'Tipin',
     'Dscc1', 'Blm', 'Casp8ap2', 'Usp1', 'Clspn', 'Pola1', 'Chaf1b', 'Brip1', 'E2f8']
g2m_genes_list = \
    ['Hmgb2', 'Cdk1', 'Nusap1', 'Ube2c', 'Birc5', 'Tpx2', 'Top2a', 'Ndc80',
     'Cks2', 'Nuf2', 'Cks1b', 'Mki67', 'Tmpo', 'Cenpf', 'Tacc3', 'Fam64a',
     'Smc4', 'Ccnb2', 'Ckap2l', 'Ckap2', 'Aurkb', 'Bub1', 'Kif11', 'Anp32e',
     'Tubb4b', 'Gtse1', 'Kif20b', 'Hjurp', 'Cdca3', 'Hn1', 'Cdc20', 'Ttk',
     'Cdc25c', 'Kif2c', 'Rangap1', 'Ncapd2', 'Dlgap5', 'Cdca2', 'Cdca8',
     'Ect2', 'Kif23', 'Hmmr', 'Aurka', 'Psrc1', 'Anln', 'Lbr', 'Ckap5',
     'Cenpe', 'Ctcf', 'Nek2', 'G2e3', 'Gas2l3', 'Cbx5', 'Cenpa']
