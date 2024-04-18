"""
dcp_to_tier1_mapping: dictionary with mapping between DCP and Tier 1 fields
tier1: tier 1 v0.3 list
hca_keys: include all fields that were available for initial kidney convertion
for updated mapping:
https://docs.google.com/spreadsheets/d/12LzqHj78CLpalRiaPIoCJcAKM1mCmzpu
"""

dcp_to_tier1_mapping = {
	'project.project_core.project_title': 'title',
	'project.contributors.name': 'study_pi',
	# none: 'batch_condition',
	# none: 'default_embedding',
	# none: 'comments',
	'specimen_from_organism.biomaterial_core.biomaterial_id': 'sample_id',
	'donor_organism.biomaterial_core.biomaterial_id': 'donor_id',
	'library_preparation_protocol.protocol_core.protocols_io_doi': 'protocol_url',
	'project.contributors.institute': 'institute',
	'sample_collection_site': 'sample_collection_site',
	'specimen_from_organism.biomaterial_core.timecourse.value': 'sample_collection_relative_time_point',
	'cell_suspension.biomaterial_core.biomaterial_id': 'library_id',
	'library_id_repository': 'library_id_repository',
	'cell_suspension.biomaterial_core.biomaterial_name': 'library_id_repository_name',
	'cell_suspension.biomaterial_core.biomaterial_description': 'library_id_repository_description',
	# 'cell_suspension.biomaterial_core.biomaterial_description': 'author_batch_notes',
	'donor_organism.biomaterial_core.ncbi_taxon_id': 'organism_ontology_term_id',
	'donor_organism.death.hardy_scale': 'manner_of_death',
	'donor_organism.death.cause_of_death': 'manner_of_death_string',
	'donor_organism.is_living': 'sample_source_alive',
    'specimen_from_organism.transplant_organ': 'sample_source_organ',
	'donor_organism.sex': 'sex_ontology_term_id',
	'collection_protocol.method.ontology_label': 'sample_collection_method',
	# none: 'tissue_type',
	'donor_organism.diseases.ontology_label': 'sampled_site_condition_donor',
	'specimen_from_organism.diseases.ontology_label': 'sampled_site_condition_specimen',
	'specimen_from_organism.organ.text': 'tissue_free_text',
	'specimen_from_organism.organ.ontology': 'tissue_ontology_term_id',
	'specimen_from_organism.organ.ontology_label': 'tissue_free_text_label',
	'specimen_from_organism.organ_parts.text': 'tissue_free_text_parts',
	'specimen_from_organism.organ_parts.ontology': 'tissue_ontology_term_id_parts',
	'specimen_from_organism.organ_parts.ontology_label': 'tissue_free_text_label_parts',
	'specimen_from_organism.preservation_storage.storage_method': 'sample_preservation_method',
	'library_preparation_protocol.nucleic_acid_source': 'suspension_type',
	'enrichment_protocol.markers': 'cell_enrichment',
	'cell_suspension.cell_morphology.percent_cell_viability': 'cell_viability_percentage',
	'cell_suspension.estimated_cell_count': 'cell_number_loaded',
	'specimen_from_organism.collection_time': 'sample_collection_year',
	'library_preparation_protocol.library_construction_method.ontology': 'assay_ontology_term_id',
	'sequence_file.library_prep_id': 'library_preparation_batch',
	'library_sequencing_run': 'library_sequencing_run',
	'library_preparation_protocol.end_bias': 'sequenced_fragment',
	'sequencing_protocol.instrument_manufacturer_model.text': 'sequencing_platform',
	# none: 'is_primary_data',
	'analysis_file.genome_assembly_version': 'reference_genome',
	'analysis_protocol.gene_annotation_version': 'gene_annotation_version',
	'analysis_protocol.alignment_software': 'alignment_software',
	'analysis_protocol.alignment_software_version': 'alignment_software_version',
	'analysis_protocol.intron_inclusion': 'intron_inclusion',
	# none: 'author_cell_type',
	# none: 'cell_type_ontology_term_id',
	'donor_organism.diseases.ontology': 'disease_ontology_term_id',
	'donor_organism.human_specific.ethnicity.ontology': 'self_reported_ethnicity_ontology_term_id',
	'donor_organism.organism_age': 'development_stage_ontology_term_id'
}
tier1 = {'uns': ['title', 'study_pi', 'batch_condition', 'default_embedding', 'comments'], 
		 'obs': ['sample_id', 'donor_id', 'protocol_url', 'institute', 'sample_collection_site', 
		 		 'sample_collection_relative_time_point', 'library_id', 'library_id_repository', 
				 'author_batch_notes', 'organism_ontology_term_id', 'manner_of_death', 
				 'sample_source', 'sex_ontology_term_id', 'sample_collection_method', 
				 'tissue_type', 'sampled_site_condition', 'tissue_ontology_term_id', 
				 'tissue_free_text', 'sample_preservation_method', 'suspension_type', 
				 'cell_enrichment', 'cell_viability_percentage', 'cell_number_loaded', 
				 'sample_collection_year', 'assay_ontology_term_id', 'library_preparation_batch', 
				 'library_sequencing_run', 'sequenced_fragment', 'sequencing_platform', 
				 'is_primary_data', 'reference_genome', 'gene_annotation_version', 
				 'alignment_software', 'intron_inclusion', 'author_cell_type', 
				 'cell_type_ontology_term_id', 'disease_ontology_term_id', 
				 'self_reported_ethnicity_ontology_term_id', 'development_stage_ontology_term_id']
}
tier1_required = {
    "MUST":
    [
        "alignment_software", "assay_ontology_term_id", "cell_enrichment", 
		"cell_type_ontology_term_id", "development_stage_ontology_term_id",
		"disease_ontology_term_id", "donor_id", "gene_annotation_version", 
		"institute", "is_primary_data", "library_id", "library_preparation_batch",
        "library_sequencing_run", "manner_of_death", "organism_ontology_term_id",
        "reference_genome", "sample_collection_method", "sample_id",
        "sample_preservation_method", "sample_source", "sampled_site_condition",
        "self_reported_ethnicity_ontology_term_id", "sequenced_fragment",
        "sex_ontology_term_id", "study_pi", "suspension_type",
		"tissue_ontology_term_id", "tissue_type", "title"
    ],
    "RECOMMENDED":
    [
        "author_batch_notes", "author_cell_type", "batch_condition",
		"cell_number_loaded", "cell_viability_percentage", "comments",
		"default_embedding", "intron_inclusion", "library_id_repository",
        "protocol_url", "sample_collection_relative_time_point",
        "sample_collection_site", "sample_collection_year",
        "sequencing_platform", "tissue_free_text"
    ]
}
hca_keys = ["analysis_file.matrix_cell_count","cell_suspension.biomaterial_core.biomaterial_id","specimen_from_organism.organ.text","specimen_from_organism.organ.ontology","specimen_from_organism.organ.ontology_label","specimen_from_organism.organ_parts.text","specimen_from_organism.organ_parts.ontology","specimen_from_organism.organ_parts.ontology_label","sequencing_protocol.instrument_manufacturer_model.text","sequencing_protocol.instrument_manufacturer_model.ontology","sequencing_protocol.instrument_manufacturer_model.ontology_label","library_preparation_protocol.library_construction_method.text","library_preparation_protocol.library_construction_method.ontology","library_preparation_protocol.library_construction_method.ontology_label","library_preparation_protocol.nucleic_acid_source","donor_organism.organism_age","donor_organism.sex","donor_organism.medical_history.test_results","donor_organism.biomaterial_core.biomaterial_description","donor_organism.medical_history.treatment","donor_organism.timecourse.value","specimen_from_organism.diseases.text","specimen_from_organism.diseases.ontology","specimen_from_organism.diseases.ontology_label","donor_organism.diseases.text","donor_organism.diseases.ontology","donor_organism.diseases.ontology_label","donor_organism.medical_history.smoking_history","donor_organism.is_living","specimen_from_organism.preservation_storage.preservation_method","donor_organism.human_specific.ethnicity.text","donor_organism.human_specific.ethnicity.ontology","donor_organism.human_specific.ethnicity.ontology_label","analysis_file.genome_assembly_version","library_preparation_protocol.cell_barcode.barcode_read","library_preparation_protocol.cell_barcode.barcode_offset","library_preparation_protocol.cell_barcode.barcode_length","library_preparation_protocol.input_nucleic_acid_molecule.text","library_preparation_protocol.input_nucleic_acid_molecule.ontology","library_preparation_protocol.input_nucleic_acid_molecule.ontology_label","library_preparation_protocol.end_bias","library_preparation_protocol.strand","library_preparation_protocol.umi_barcode.barcode_read","library_preparation_protocol.umi_barcode.barcode_offset","library_preparation_protocol.umi_barcode.barcode_length","sequencing_protocol.10x.fastq_method","sequencing_protocol.method.text","sequencing_protocol.method.ontology","sequencing_protocol.method.ontology_label","cell_suspension.biomaterial_core.biosamples_accession","cell_suspension.biomaterial_core.insdc_sample_accession","cell_suspension.growth_conditions.culture_environment","cell_suspension.selected_cell_types.text","cell_suspension.selected_cell_types.ontology","cell_suspension.selected_cell_types.ontology_label","cell_suspension.plate_based_sequencing.plate_label","enrichment_protocol.method.text","enrichment_protocol.method.ontology","enrichment_protocol.method.ontology_label","enrichment_protocol.markers","enrichment_protocol.maximum_size","dissociation_protocol.method.text","dissociation_protocol.method.ontology","dissociation_protocol.method.ontology_label","specimen_from_organism.adjacent_diseases.text","specimen_from_organism.adjacent_diseases.ontology","specimen_from_organism.adjacent_diseases.ontology_label","specimen_from_organism.preservation_storage.storage_time","collection_protocol.method.text","collection_protocol.method.ontology","collection_protocol.method.ontology_label","donor_organism.human_specific.body_mass_index","donor_organism.death.cause_of_death","donor_organism.medical_history.alcohol_history","donor_organism.medical_history.medication","donor_organism.gestational_age","donor_organism.gestational_age_unit.text","aggregate_generation_protocol.protocol_core.protocols_io_doi","analysis_file.genome_patch_version","analysis_protocol.protocol_core.protocols_io_doi","cell_line.biomaterial_core.biomaterial_description","cell_line.biomaterial_core.biomaterial_id","cell_line.biomaterial_core.biomaterial_name","cell_suspension.biomaterial_core.biomaterial_description","cell_suspension.biomaterial_core.biomaterial_name","cell_suspension.cell_morphology.percent_cell_viability","cell_suspension.estimated_cell_count","collection_protocol.protocol_core.protocols_io_doi","differentiation_protocol.protocol_core.protocols_io_doi","dissociation_protocol.protocol_core.protocol_id","dissociation_protocol.protocol_core.protocols_io_doi","dissociation_protocol.protocol_core.protocol_description","donor_organism.biomaterial_core.biomaterial_id","donor_organism.biomaterial_core.biomaterial_name","donor_organism.biomaterial_core.timecourse.relevance","donor_organism.biomaterial_core.timecourse.unit.text","donor_organism.biomaterial_core.timecourse.unit.ontology","donor_organism.biomaterial_core.timecourse.unit.ontology_label","donor_organism.biomaterial_core.timecourse.value","donor_organism.development_stage.text","donor_organism.development_stage.ontology","donor_organism.development_stage.ontology_label","donor_organism.genus_species.text","donor_organism.genus_species.ontology","donor_organism.genus_species.ontology_label","donor_organism.biomaterial_core.ncbi_taxon_id","donor_organism.gestational_age_unit.text","donor_organism.gestational_age_unit.ontology","donor_organism.gestational_age_unit.ontology_label","donor_organism.human_specific.ethnicity.text","donor_organism.organism_age_unit.text","donor_organism.organism_age_unit.ontology","donor_organism.organism_age_unit.ontology_label","enrichment_protocol.protocol_core.protocols_io_doi","imaged_specimen.biomaterial_core.biomaterial_description","imaged_specimen.biomaterial_core.biomaterial_name","imaging_preparation_protocol.protocol_core.protocols_io_doi","imaging_protocol.protocol_core.protocols_io_doi","ipsc_induction_protocol.protocol_core.protocols_io_doi","library_preparation_protocol.library_construction_method.text","library_preparation_protocol.protocol_core.protocols_io_doi","organoid.biomaterial_core.biomaterial_description","organoid.biomaterial_core.biomaterial_name","project.contributors.corresponding_contributor","project.contributors.institution","project.contributors.name","project.contributors.project_role.text","project.contributors.project_role.ontology","project.contributors.project_role.ontology_label","project.publications.doi","sequence_file.lane_index","sequencing_protocol.protocol_core.protocols_io_doi","specimen_from_organism.biomaterial_core.biomaterial_description","specimen_from_organism.biomaterial_core.biomaterial_id","specimen_from_organism.biomaterial_core.biomaterial_name","specimen_from_organism.biomaterial_core.timecourse.relevance","specimen_from_organism.biomaterial_core.timecourse.unit.text","specimen_from_organism.biomaterial_core.timecourse.unit.ontology","specimen_from_organism.biomaterial_core.timecourse.unit.ontology_label","specimen_from_organism.biomaterial_core.timecourse.value","specimen_from_organism.collection_time","specimen_from_organism.preservation_storage.storage_method","treatment_protocol.protocol_core.protocols_io_doi"]
# Code to include all hca fields
# import pandas as pd
# hca_template_url = 'https://github.com/ebi-ait/geo_to_hca/raw/master/template/hca_template.xlsx'
# dcp_spreadsheet = pd.read_excel(hca_template_url, sheet_name=None, skiprows= [0,1,2,4])
# all_hca = set()
# for tab_name, tab in dcp_spreadsheet.items():
#     all_hca.update(tab.columns)
